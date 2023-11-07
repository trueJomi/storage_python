from pydantic import BaseModel, Field

class ResponseIamge3(BaseModel):
    introducction: dict = Field({})
    middle: dict = Field({})
    end: dict = Field({})