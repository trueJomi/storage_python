import requests
from concurrent.futures import ThreadPoolExecutor
from aplication.models_endpoint.images_text_input import ImageTextInput
from domain.models.image_entity_send import SendQueryIamgeEntity

API_URL="https://600d-2001-1388-28a1-a6d5-11f6-7491-3923-3864.ngrok-free.app/"

def image_obtain(prompt:str):
    message_api= SendQueryIamgeEntity(prompt)
    response =requests.post(
        f"{API_URL}/sdapi/v1/txt2img",
        headers={
            'Content-Type': 'application/json',
        },
        json=message_api.to_dict())
    if (response.status_code >= 400):
        raise Exception(response.json()["detail"])
    json_image = response.json()
    return json_image



def concurrent_calls(
    init: str, middle: str, final: str):
    with ThreadPoolExecutor(max_workers=3) as executor:
        init_promise = executor.submit(image_obtain, init)
        middle_promise = executor.submit(image_obtain, middle)
        final_promise = executor.submit(image_obtain, final)
    init = init_promise.result()
    middle = middle_promise.result()
    final = final_promise.result()
    return {
        "init":init,
        "middle":middle,
        "final":final
    }
    
# def lineal_call(body:ImageTextInput):
#     init = image_obtain(body.init)
#     middle = image_obtain(body.middle)
#     final = image_obtain(body.final)
#     return {
#         "init":init,
#         "middle":middle,
#         "final":final
#     }
