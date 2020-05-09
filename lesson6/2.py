#в одну строку записвается имя_человека,возраст
#yerassyl 19.01.1998
line = input()#yerassyl,22
parts = line.split(" ")#["yerassyl","22"]
d={}
d['name']=parts[0]
d['age']=int(parts[1])
print(d)