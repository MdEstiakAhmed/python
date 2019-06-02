import requests
img_url = "http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c51f.png"

res = requests.get(img_url)

with open("create_with_python.png", "wb") as f:
    f.write(res.content)