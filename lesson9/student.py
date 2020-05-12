class Student:
    def __init__(self,name,age,marks):
        self.name =name
        self.age = age
        self.marks =marks
    
    def getAverageMark(self):
        sumi=0
        n = len(self.marks)
        for i in self.marks:
            sumi= sumi +i
        return sumi/n
    def __str__(self):
        avg = self.getAverageMark()
        return f"Name:{self.name},Age:{self.age},Marks:{self.marks},AverageMark:{avg}"