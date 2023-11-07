from instructure.storage import save_image
from domain.utils.base64_to_image import to_image

img_name="eb0f49c1-50ec-4c76-9fcd-41eaa796366d"

def test_tranform_base64_to_image():
    with open('tests/static/bin.txt', 'rb') as file:
        image_bytes = file.read()
        array_bytes= bytearray(image_bytes)
        image = to_image(array_bytes)
    assert type(image['id']) is str
    assert type(image['direction']) is str

def test_save_image():
    url = save_image(f"domain/static/temp/{img_name}.png", f"{img_name}.png")
    assert type(url) is str