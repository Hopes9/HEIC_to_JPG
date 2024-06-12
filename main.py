import os
from PIL import Image
import pyheif

input_folder = '/Users/hopes98/Desktop/photos'
output_folder = '/Users/hopes98/Desktop/jpg'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".heic"):
        heif_file = pyheif.read(os.path.join(input_folder, filename), convert_hdr_to_8bit=True, apply_transformations=True)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )
        image.save(os.path.join(output_folder, filename.replace(".heic", ".jpg")), "JPEG")
