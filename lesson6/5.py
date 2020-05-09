# 2
# yerassyl,22,5 3 4 5
# kirito,20,5 3 2 4
n = int(input())#2
students=[]
for i in range(n):
    line = input()#yerassyl,22,5 3 4 5
    parts = line.split(",")#['yerassyl', '22', '5 3 4 5']
    name = parts[0]
    age = int(parts[1])
    marks_str = parts[2]
    marks_str_arr = marks_str.split(" ")#['5','3','4','5']
    marks_int_arr = [int(i) for i in marks_str_arr]#[5,3,4,5]
    d={}
    d['name']=name
    d['age']=age
    d['marks']=marks_int_arr
    students.append(d)

# for i in students:
#     i['test_precent'] = i['marks'][0]/i['marks'][1]    

for i in students:
    print(i)
# [
#     {
#         "name":"yerasyl",
#         "age":22,
#         "marks":[5,3,4,5]
#     },
#     {

#     },

# ]