class Post:
    def __init__(self,id,userid,title,body):
        self.userId=userid
        self.id=id
        self.title = title
        self.body = body
    def getBody(self):
        return self.body

    def __str__(self):
        st = f"Id:{self.id},UserId:{self.userId},Title:{self.title}"
        return st
    