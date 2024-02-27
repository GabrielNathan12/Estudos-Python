from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORI = ROOT_FOLDER / 'image.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'


pil_image = Image.open(ORI)
width, height = pil_image.size

new_width = 10000
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(NEW_IMAGE, optimize=True, quality=100)
#print(new_width, new_height)