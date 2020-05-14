'''python files'''
x=[]
for i in range(1,11):
    x.append(i**2)
print(x)
x2=[i**2 for i in range(1,12)]
print(x2)
d=[]
for i in range(1,10):
    d.append(-i)
print(d)
d2=[-i for i in range(1,11)]
print(d2)
name=['harshit','mohit','rohit']
na=[]
for i in name:
    na.append(i[0])

print(na)
na2=[i[0] for i in name]
print(na2)
'''111isnan'''