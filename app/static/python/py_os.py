import os

def delete_file(folder_name, file_name):
    os.unlink("../images/car/" + folder_name + "/" + file_name)

def delete_folder(folder_name):
    os.unlink("../images/car/" + folder_name)

def create_folder(folder_name):
    os.mkdir("../images/car/" + folder_name)

# print(os.path.dirname(__name__))