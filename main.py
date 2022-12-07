import json

with open("elementos.json", "r") as f:
    f = json.load(f)
    print(f)
    print(type(f))