import base64, json
from pathlib import Path

def encode():
    global encoded_image, suffix, name, file_count
    file_count = 0
    name = []
    suffix = []
    encoded_image = []
    for file in Path("upload").iterdir():
        with open(file, "rb") as image:
            data_binary = image.read()
            encoded_image = base64.b85encode(data_binary).decode()
            suffix = file.suffix
            name = file.stem
            file_count = file_count + 1
            file_properties = {"encoded image": encoded_image, "suffix": suffix, "name": name, "file count": file_count}
            with open(f"file_properties/{name}{suffix}.json", "w") as properties:
                json.dump(file_properties, properties, indent=4)


def decode():
    for file_num in range(file_count):
        decoded_image = base64.b85decode(encoded_image[file_num])
        with open(f"download/{name[file_num]}{suffix[file_num]}", "wb") as restored:
            restored.write(decoded_image)

encode()
decode()
