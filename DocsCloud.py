
import base64, json
from pathlib import Path

def encode():
    global encoded_image, suffix, name, file_count
    file_count = 0
    name = []
    suffix = []
    for file in Path("upload").iterdir():
        with open(file, "rb") as image:
            data_binary = image.read()
            encoded_image = base64.b85encode(data_binary).decode()
            suffix.append(file.suffix)
            name.append(file.stem)
            file_count = file_count + 1

def decode():
    decoded_image = base64.b85decode(encoded_image)
    for file_num in range(file_count):
        with open(f"download/{name[file_num]}{suffix[file_num]}", "wb") as restored:
            restored.write(decoded_image)
