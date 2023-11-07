import os
from instructure.storage import save_image
from urllib.request import urlretrieve
import uuid

def save_image_storage_with_url_service(url:str):
    id = str(uuid.uuid4())
    directory = f"domain/static/temp/{id}.png"
    urlretrieve(url, directory)
    image_path = save_image(directory, f"{id}.png")
    os.remove(directory)
    return {
        "id": id,
        "path_storage": image_path,
        "params": {
            "prompt": "no"
        }
    }
