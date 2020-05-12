#Dog-(name,realage)
#call()->"Gav"
#create class
#class variable
#object variable
class Person:
    #constructor
    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def doSomething(self):
        return "hello"
    
    def getYear(self):
        return 2020-self.age



#create object
p1 = Person("kirito",98)
p2 = Person("yerassyl",22)
print(p1.name,p1.doSomething(),p1.getYear())
print(p2.name,p1.doSomething(),p2.getYear())