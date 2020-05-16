import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.text
posts = json.loads(json_data)
#id-indentifier of post it create when user create post
#userId-identifuer about user
for i in posts:
    print(i)