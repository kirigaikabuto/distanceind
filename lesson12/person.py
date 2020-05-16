class Person:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def __str__(self):
        st = f"Name:{self.name},Password:{self.password}"
        return st