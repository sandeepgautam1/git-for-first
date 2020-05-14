inm = input("enter your name:")
i = 0
print(f"{inm.count(inm)}")
tem = ""
while i<len(inm):
    if inm[i] not in tem:
        tem+=inm[i]
        print(f"{inm[i]}:{inm.count(inm[i])}")
    i+=1

