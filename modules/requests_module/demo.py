import requests
import os
import webbrowser as wb

url = "http://example.com/"
res = requests.get(url)

with open("demo.html", "w", encoding=res.encoding) as f:
    f.write(res.text)

file_path = os.path.realpath("demo.html")
print(file_path)
wb.open("file://" + file_path)
