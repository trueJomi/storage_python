from PIL import Image
import io
import base64
import uuid

def to_image(str_byte_array:str):
    bytes_data=str_byte_array.encode("utf-8")
    array_bytes= bytearray(bytes_data)
    data_b = base64.b64decode(array_bytes)
    image = Image.open(io.BytesIO(data_b))
    id = str(uuid.uuid4())
    direction = f"domain/static/temp/{id}_uopt.png"
    image.save(direction)
    direction = f"domain/static/temp/{id}.png"
    return {
        "id": id,
        "direction":direction
    }
