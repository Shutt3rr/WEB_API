import requests 
from PIL import Image
from io import BytesIO

def get_dog():
  url = "https://api.thedogapi.com/v1/images/search"
  response = requests.get(url)
  print(response)
  data = response.json()
  print(data)
  image = requests.get(data[0]["url"])
  img = Image.open(BytesIO(image.content))
  title = "Random Dog"
  img.save(f"./doggy/{title}.jpg")

get_dog()


