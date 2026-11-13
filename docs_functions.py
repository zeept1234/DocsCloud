from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json
from pathlib import Path
from time import sleep
from rich import print

def auth():
    creds = Credentials.from_authorized_user_file("token.json")
    service = build("docs", "v1", credentials=creds)
    return service

def create_doc(service, batch):
    document = service.documents().create(
        body={"title": f"Batch_{batch}_DocsCloud"}
    ).execute()
    document_id = document["documentId"]

    doc_info = {"batch": batch, "document_id": document_id}

    with open(f"batch/batch_{batch}", "w") as file:
        json.dump(doc_info, file, indent=4)

    return document_id

def send_to_doc(service, document_id, json_info):
    service.documents().batchUpdate(
        documentId = document_id,
        body = {
            "requests": [
                {
                    "insertText": {
                        "endOfSegmentLocation": {},
                        "text": json_info
                    }
                }
            ]
        }
    ).execute()

def get_text(service, document_id):
    document = service.documents().get(
        documentId = document_id
        ).execute()

    text_run = []

    for body in document["body"]["content"]:
        if "paragraph" in body:
            for content in body["paragraph"]["elements"]:
                if "textRun" in content:
                    text_run.append(content["textRun"]["content"])

    text = "".join(text_run)
    return text

def upload(service, document_id):
    batch = get_batch()

    max_len = 1_000_000 #Sets max length
    overflow = []

    for json_file in Path("file_properties").iterdir(): #Loops every json for upload
        if json_file.name == "README.md": #Ignores README.md
            continue
        with open (json_file) as file_properties: #Saves the json in a string and dictionary
            json_properties_string = file_properties.read()
            json_properties = json.loads(json_properties_string)

        doc_len = get_length(service, document_id) #Checks current length of document
        new_len = len(json_properties_string) #Checks length of json
 
        if new_len > max_len: #Checks if the json is too large
            overflow.append(json_properties["name"])
            continue
        elif doc_len + new_len > max_len: #Checks if the added json overflows the doc
            batch = batch + 1 #Creates a new batch and document to store json
            with open("batch/batch.json", "w") as file:
                batch_dict = {"batch": batch}
                json.dump(batch_dict, file, indent=4)
            document_id = create_doc(service, batch)
            try:
                send_to_doc(service, document_id, json_properties_string)
            except:
                return "Fail", "Failed to upload"
            else:
                json_file.unlink()
        else: 
            try:
                send_to_doc(service, document_id, json_properties_string)  
            except:
                return "Fail", "Failed to upload"
            else:
                json_file.unlink()
    if overflow != []:
        return "Fail", overflow
    return "Success", "Success"

def get_length(service, document_id): #Gets document length
    document = service.documents().get(
        documentId = document_id,
        fields = "body/content(endIndex)"
    ).execute()
    length = document["body"]["content"][-1]["endIndex"] - 2
    return length

def get_document_id(batch):
    service = auth()
    for batch_json in Path("batch").iterdir():
        if batch_json.name == "batch.json":
            continue
        with open(batch_json) as file:
            json_batch = json.load(file)
            if batch == json_batch["batch"]:
                if json_batch["document_id"] == None:
                    document_id = create_doc(service, batch)
                    return document_id
                return json_batch["document_id"]

def get_batch():
    with open("batch/batch.json") as file:
        batch = json.load(file)
        return batch["batch"]

def download(service, batch):
    decoder = json.JSONDecoder()
    position = 0
    count = 0

    if batch == "all": 
        for batch_all in Path("batch").iterdir():
            position = 0
            if batch_all.name == "batch.json":
                continue
            with open(batch_all, "r") as file:
                document_id_dict = json.load(file)
                document_id = document_id_dict["document_id"]
                text = get_text(service, document_id).strip()
            while position < len(text):
                json_properties, position = decoder.raw_decode(text, position)

                with open(f"file_properties/{json_properties['name']}{json_properties['suffix']}.json", "w") as file:
                    json.dump(json_properties, file, indent=4)
                count = count + 1

                while position < len(text) and text[position].isspace():
                    position = position + 1

    elif isinstance(batch, int):
        document_id = get_document_id(batch)
        if document_id is None:
            outcome = "Fail"
            return outcome, None
        text = get_text(service, document_id).strip()
        while position < len(text):
            json_properties, position = decoder.raw_decode(text, position)

            with open(f"file_properties/{json_properties['name']}{json_properties['suffix']}.json", "w") as file:
                json.dump(json_properties, file, indent=4)
            count = count + 1

            while position < len(text) and text[position].isspace():
                position = position + 1

    else:
        max_batch = get_batch()
        output = print(f"[red]Batch must be number 0 - {max_batch} or 'all'")
        return output

    if count != 1:
        s = "s"
    else:
        s = ""
    return s, count

if __name__ == "__main__":
    pass