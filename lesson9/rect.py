class Rectangle:
    def __init__(self,a,b):
        self.width = a
        self.height = b
    
    def calculateP(self):
        return 2*(self.width+self.height)

    def __str__(self):
        return f"Rectangle object:{self.width},{self.height}"