import requests
img_url = "https://sci-hub.tw/10.1109/ICSCET.2018.8537299"

res = requests.get(img_url, stream=True)

with open("new.pdf", "wb") as f:
    f.write(res.content)