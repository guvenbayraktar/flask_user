from config import UPLOAD_FOLDER
from uuid import uuid4

# kullanıcının eklediği resimleri kaydeden fonk.


def save_profile_picture(input_file, extension):
    filename = str(uuid4()) + "." + extension
    full_path = UPLOAD_FOLDER + "/" + filename
    with open(full_path, "wb") as output_file:
        output_file.write(input_file.read())
    return full_path
