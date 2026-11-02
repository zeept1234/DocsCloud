
import base64
import json
from pathlib import Path


def encode():
    global encoded_image, suffix, name
    for file in Path("upload").iterdir():
        with open(file, "rb") as image:
            data_binary = image.read()
            encoded_image = base64.b85encode(data_binary).decode()
            suffix = file.suffix
            name = file.stem

def decode():
    decoded_image = base64.b85decode(encoded_image)
    with open(f"download/{name}{suffix}", "wb") as restored:
        restored.write(decoded_image)


encode()
decode()