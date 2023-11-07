from pydantic import BaseModel, Field

class ResponseEntityImage(BaseModel):
    id: str = Field("id")
    path_storage: str = Field("ubicacion de la imagen")
    params: dict = Field({})