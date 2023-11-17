from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from aplication.controllers.image_controllers import image_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(image_router)    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True ,  port=5200, workers=4)