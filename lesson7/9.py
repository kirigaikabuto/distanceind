from mytools import *
def getData(d):
    name = d['name']
    age = d['age']
    s=f"Name:{name},Age:{age}"
    return s
users=[
    {
        "name":"name1",
        "age":22
    },
    {
        "name":"name2",
        "age":23
    },
]
full_users = list(map(getData,users))
print(full_users)