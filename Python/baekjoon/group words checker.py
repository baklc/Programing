c=0
n=int(input())
for k in range(n):
    l=0
    a=input()
    for i in range(len(a)):
        if i==len(a)-1:
            c+=1
            break
        elif a[i]==a[i+1]:
            pass
        elif a[i] in a[i+1:]:
            break
print(c)