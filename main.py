from docs_functions import *
from codec_functions import *

def get_user_choice():
    user_choice = int(input("Choose action:\n1. Encode: Encodes the files in the 'upload/' folder to base85 and stores it in 'file_properties/' temporarily\n2. Upload: Sends the files from 'upload/' to Google Docs for cloud storage\n3. Download: Retrieves the file properties from Google Docs and stores it in 'file_properties/' temporarily\n4. Decode: Turns the files storing base85 in 'file_properties/' to the original files and puts them in 'downloads/'\nInput here --> "))
    return user_choice

def action():
    service = auth()
    user_choice = get_user_choice()
    if user_choice == 1: #Encode
        encode()
        action()
    elif user_choice == 2: #Upload
        batch = get_batch()
        document_id = get_document_id(batch)
        upload(service, document_id)
        action()
    elif user_choice == 3: #Download
        batch_max = get_batch()
        batch = int(input(f"Select batch to download from batches 0 - {batch_max}: "))
        download(service, batch)
        action()
    elif user_choice == 4: #Decode
        decode()
        action()
    else:
        print("Invalid selection")
        action()

if __name__ == "__main__":
    action()