import base64, json
from pathlib import Path

def encode():
    for file in Path("upload").iterdir():
        if file.name == "README.md":
            continue
        print(file)


def decode():
    for file_num in Path("file_properties").iterdir(): 
        with open(f"download/{json_store["name"]}{json_store["suffix"]}", "wb") as json_store:
            file_properties = json.load(json_store)
            decoded_image = base64.b85decode(file_properties["encoded image"])
            json_store.write(decoded_image)

encode()

