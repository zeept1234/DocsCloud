import base64, json
from pathlib import Path

def encode():
    name = []
    suffix = []
    encoded_image = []
    for file in Path("upload").iterdir():
        if file.name == "README.md":
            continue
        with open(file, "rb") as image:
            data_binary = image.read()
            encoded_image = base64.b85encode(data_binary).decode()
            suffix = file.suffix
            name = file.stem
            file_properties = {"encoded image": encoded_image, "suffix": suffix, "name": name}
            with open(f"file_properties/{name}{suffix}.json", "w") as properties:
                json.dump(file_properties, properties, indent=4)


def decode():
    for file_num in Path("file_properties").iterdir(): 
        if file_num.name == "README.md":
            continue
        with open(file_num) as properties:
            file_properties = json.load(properties)
        with open(f"download/{file_properties["name"]}{file_properties["suffix"]}", "wb") as restored:
            decoded_image = base64.b85decode(file_properties["encoded image"])
            restored.write(decoded_image)

decode()