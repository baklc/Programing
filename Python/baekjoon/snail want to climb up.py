a=[3,1,5]
c=0
d=0
n=a[0]-a[1]
l=a[2]//n
if n==1:
    print(l-a[1])
elif l*a[0]+a[0]>=a[2]:
    print(l+1)