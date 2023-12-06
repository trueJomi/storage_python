import requests
from concurrent.futures import ThreadPoolExecutor
from domain.models.image_entity_send import SendQueryIamgeEntity

API_URL = "http://localhost:7861"
# API_URL="https://4afb-2001-1388-28a1-170d-cd8-4472-81e5-cbdd.ngrok-free.app"

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

def exist():
    response = requests.get(
        f'{API_URL}/docs',
    )
    if (response.status_code >= 400):
        raise Exception(response.json()["detail"])
    return True

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