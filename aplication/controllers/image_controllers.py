from aplication.controllers import image_router
from aplication.models_endpoint.response_entity_image import ResponseEntityImage
from fastapi import status, HTTPException
from aplication.models_endpoint.image_input import ImageQuery
from domain.utils.token import comprare_token
from domain.services.image_services import get_1_image_service, get_3_image_service
from aplication.models_endpoint.images_text_input import ImageTextInput
from domain.services.save_image_url_services import save_image_storage_with_url_service
from aplication.models_endpoint.url_input import QueryImageSave
from aplication.models_endpoint.image_3_response import ResponseIamge3

@image_router.post(
    "/getImage",
    status_code = status.HTTP_201_CREATED,
    response_model= ResponseEntityImage
    )
def create_1_image(body:ImageQuery):
    if not comprare_token(body.token):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: Unauthorized API"
        )
    # try:
    data=get_1_image_service(body.prompt)
    return data.to_dict()
    # except Exception as e:
    #     raise HTTPException(
    #         status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f"Error: {e}"
    #     )

@image_router.post(
    "/get3Images",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseIamge3
)
def images3(body:ImageTextInput):
    if not comprare_token(body.token):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: Unauthorized API"
        )
    try:
        result_data = get_3_image_service(body.init, body.middle, body.final)
        return result_data.to_dict()
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

@image_router.post(
    "/saveImage",
    status_code=status.HTTP_201_CREATED,
    response_model= ResponseEntityImage
)
def save_image_url(body:QueryImageSave):
    if not comprare_token(body.token):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: Unauthorized API"
        )
    try:
        result_data = save_image_storage_with_url_service(body.url)
        return result_data
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
     