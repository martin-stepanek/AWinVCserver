import requests
import json
import pprint

# Try with local server - https://github.com/typicode/json-server
response = requests.get("http://localhost:3000/posts")
response.json()

# New data need to be posted in one of the existing locations in db.json - e.g. /posts
r = requests.post("http://localhost:3000/posts", json={"key": "value"})

# Try with the typicode solution - doesn't work veryw ell
# response = requests.get("https://my-json-server.typicode.com/martin-stepanek/AWinVC/posts")
# print(response.text)

# Try with fakejson
payload = {
    "token": "BjbwTrsK1uCxeZuLLh9anw",
    "data": {
      "id": 1,
      "value": "test"
    }
};
r = requests.post("https://app.fakejson.com/q", json = payload)

r = requests.get("https://app.fakejson.com/q", headers={"token": "BjbwTrsK1uCxeZuLLh9anw"})
print(r)
print(response.text)