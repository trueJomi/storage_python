import tinify
from domain.utils.token import TOKEN_TINY
from os import remove
tinify.key=TOKEN_TINY

def optimize_images(id:str):
    image = tinify.from_file(f"domain/static/temp/{id}_uopt.png")
    image.to_file(f"domain/static/temp/{id}.png")
    remove(f"domain/static/temp/{id}_uopt.png")
    