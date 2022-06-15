import firebase_admin
from firebase_admin import credentials, storage
import sys


cred = credentials.Certificate("app/static/python/stageiut-firebase_config.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'stageiut-e1349.appspot.com'})
bucket = storage.bucket()



def firebase_upload_file(car_id, file_name, image_id):
    blob = bucket.blob("images/cars/" + str(car_id) + "/" + str(image_id) + ".jpg")
    blob.upload_from_filename(filename=file_name)
    return True

def firebase_get_image_url(car_id, image_id):
      blob = bucket.blob("images/cars/" + str(car_id) + "/" + str(image_id) + ".jpg")
      blob.make_public()
      return blob.public_url
    
def firebase_delete_image(car_id, image_id):
      """Delete image from storage"""
      blob = bucket.blob("images/cars/" + str(car_id) + "/" + str(image_id) + ".jpg")
      blob.delete()
      return True

def firebase_edit_image(car_id, image_id, file_name):
      """Edit image from storage"""
      blob = bucket.blob("images/cars/" + str(car_id) + "/" + str(image_id) + ".jpg")
      blob.delete()
      blob.upload_from_filename(filename=file_name)
      return True
  