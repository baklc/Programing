a,n=map(int,input().split())
l=0
c=[]
for i in range(a):
    c.append(int(input()))
c.reverse()
q=0
for i in c:
    q+=n//i
    n=n%i
print(q)