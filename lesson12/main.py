import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.text
posts = json.loads(json_data)
#id-indentifier of post it create when user create post
#userId-identifuer about user
def showPosts(posts):
    for i in posts:
        print(i)
def getDataByUserId(userID):
    needed_posts=[]
    for i in posts:
        if i['userId'] == userID:
            needed_posts.append(i)
    return needed_posts

myposts = getDataByUserId(10)
for i in myposts:
    title = i['title']
    title_words = title.split(" ")
    if "nam" in title_words:
        print(title)