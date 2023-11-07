from  pydantic import BaseModel, Field 

class ImageTextInput(BaseModel):
    init: str = Field("kid sidown chair in beach")
    middle: str = Field("kid sidown chair in beach")
    final: str = Field("kid sidown chair in beach")
    token: str = Field("1234567890")