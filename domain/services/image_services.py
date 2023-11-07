from domain.utils.obtain_image import image_obtain
from domain.utils.base64_to_image import to_image
from instructure.storage import save_image
from os import remove
from concurrent.futures import ThreadPoolExecutor
from domain.services.save_image_url_services import save_image_storage_with_url_service

def get_1_image_service( prompt:str):
    json_image =image_obtain(prompt)
    image_str = json_image["images"][0]
    image = to_image(image_str)
    path =save_image(image["direction"], f"{image['id']}.png")
    remove(image["direction"])
    return {
        "id":image['id'],
        "path_storage":path,
        "params": json_image["parameters"]
    }
    
def get_3_image_service(
    init_prompt: str, middle_prompt: str, final_prompt: str
    ):
    with ThreadPoolExecutor(max_workers=3) as executor:
        init_promise = executor.submit(get_1_image_service, init_prompt)
        middle_promise = executor.submit(get_1_image_service, middle_prompt)
        final_promise = executor.submit(get_1_image_service, final_prompt)
    init = init_promise.result()
    middle = middle_promise.result()
    final = final_promise.result()
    return {
        "introducction":init,
        "middle":middle,
        "end":final
    }