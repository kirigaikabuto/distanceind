import requests
import json
from post import Post
from posts import Posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.text
posts = json.loads(json_data)
#keys=posts[0].keys()
#print(keys)
#create Post objects and append it to objects list
objects=[]
for i in posts:
    post = Post(i['id'],i['userId'],i['title'],i['body'])
    objects.append(post)

#create Posts object 
postsObject = Posts(objects)
postsObject.showAllPosts()
# needed_posts = postsObject.getPostByUserId(1)
# for i in needed_posts:
#     print(i)