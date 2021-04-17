a=int(input())
b=sorted(map(int,input().split()))
c=0
for i in range(a):
    for k in range(1,i+1):
        c+=b[k]
print(c)