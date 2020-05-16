class Posts:
    def __init__(self,objects):
        self.objects = objects

    def getPostByUserId(self,userId):
        needed_posts=[]
        for i in self.objects:
            if i.userId == userId:
                needed_posts.append(i)
        return needed_posts
    def showAllPosts(self):
        for i in self.objects:
            print(i)