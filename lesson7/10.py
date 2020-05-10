from mytools import *
def doReform(d):
    name = d['name']
    age = d['age']
    line = name.split(" ")
    first_name = line[0]
    last_name = line[1]
    newd={}
    newd['first_name']=first_name
    newd['last_name']=last_name
    newd['age']=age
    return newd
users=[
    {
        "name":"Tleugazy Yerassyl",
        "age":22
    },
    {
        "name":"Kirito Kirigai",
        "age":23
    },
]
full_users = list(map(doReform,users))
print_arr(full_users)
# [
#     {
#         "first_name":,
#         "last_name":,
#         "age":,
#     }
# ]