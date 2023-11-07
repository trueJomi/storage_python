from pydantic import BaseModel, Field 

class QueryImageSave(BaseModel):
    url: str = Field("url de la imagen")
    token:str = Field("token de la imagen")