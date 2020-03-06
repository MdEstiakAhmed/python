import json

with open('user.json') as json_data:
    d = json.load(json_data)    
    print(d)