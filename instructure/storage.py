import pyrebase
from instructure.config.config import firebaseConfig

firestore = pyrebase.initialize_app(firebaseConfig)
storage = firestore.storage()

def save_image(image_direction, name):
    storage.child(f"images/{name}.png").put(image_direction, content_type="image/png")
    return f"images/{name}"