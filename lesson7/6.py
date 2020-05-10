import random
from mytools import *
#yerassyl,1 2 3 4 5
line = input()#yerassyl,1 2 3 4 5
parts = line.split(",")#['yerassyl','1 2 3 4 5']
name = parts[0]
marks_str = parts[1]
marks_str_arr= marks_str.split(" ")
marks_int_arr= [int(i) for i in marks_str_arr]
d={}
d['name']=name
d['marks']=marks_int_arr
print(d)
d['max_mark']=get_max(d['marks'])
print(d)