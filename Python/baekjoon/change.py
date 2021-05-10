n=[500,100,50,10,5,1]
a=int(input())
b=1000-a
c=0
for i in n:
    c+=b//i
    b=b%i
print(c)