import base64, json
from pathlib import Path
from docs_functions import * #Add comment with functions

def encode():
    batch = get_batch()
    for file in Path("upload").iterdir(): #Loops through everything in upload folder
        if file.name == "README.md": #Skips README.md
            continue
        with open(file, "rb") as image: #Opens the file (being looped) as "image"
            data_binary = image.read()
            encoded_image = base64.b85encode(data_binary).decode()
            suffix = file.suffix
            name = file.stem
            file_properties = {"encoded image": encoded_image, "suffix": suffix, "name": name, "batch": batch}
            with open(f"file_properties/{name}{suffix}.json", "w") as properties: #Stores the stem, suffix and batch into a json
                json.dump(file_properties, properties, indent=4)
        file.unlink()

def decode():
    for file in Path("file_properties").iterdir(): 
        if file.name == "README.md":
            continue
        with open(file) as properties:
            file_properties = json.load(properties)
        with open(f"download/{file_properties["name"]}{file_properties["suffix"]}", "wb") as restored:
            decoded_image = base64.b85decode(file_properties["encoded image"])
            restored.write(decoded_image)
        file.unlink()

if __name__ == "__main__":
    pass