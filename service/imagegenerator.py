import openai
import urllib.request
from datetime import datetime

key = "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"
openai.api_key = key

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

file_name = "image"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
urllib.request.urlretrieve(image_url, file_name)