import jwt
import json

def jsonRead():
    with open("./Configuration/appsettings.json", "r"):
         data = json.load()
         
payload = {
    "sub": "4343",
    "name": "Jessica forrest",
    "nickname": "Jess"
}

token = jwt.encode(
    payload=payload_data,
    key=["JWT":"Secret"]
) 
