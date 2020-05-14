#list with if
sl=list(range(1,11))
sm =[]
for i in sl:
    if i%2==0:
        sm.append(i)
print(sm)
sn=[i for i in range(1,12) if i%2!=0]
print(sn)
sd=[i for i in range(1,10) if i%2==0]
print(sd)