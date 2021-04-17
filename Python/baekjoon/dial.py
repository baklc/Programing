import math
a=list(input())
n=[]
for i in a:
    if i=="Z":
        n.append(9)
    else:
        if ord(i)>80:
            c=3.01
        else:
            c=3
        n.append(math.floor(((ord(i)-65)/c)+2))
r=0
for i in n:
    r+=i+1
print(r)