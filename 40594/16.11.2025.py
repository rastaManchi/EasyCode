import requests, random
from PIL import Image
from io import BytesIO


width = random.randint(100, 800)
r = requests.get(f"https://placebear.com/{width}/400")
image = Image.open(BytesIO(r.content))
image.save('output.jpg')