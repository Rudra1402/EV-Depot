from django.core.files.storage import default_storage
from firebase_admin import storage
import os

def upload_image_to_firebase(file, folder_name):
    bucket = storage.bucket()
    
    filename = os.path.join(folder_name, file.name)
    
    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=file.content_type)
    
    blob.make_public()
    
    return blob.public_url