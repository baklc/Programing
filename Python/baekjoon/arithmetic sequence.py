n=int(input())
c=0
for i in range(1,n+1):
    if i < 1:
        break
    elif i < 100:
        c+=1
    elif i ==1000:
        pass
    else:
        l=str(i)
        if (int(l[1])-int(l[0])==(int(l[2])-int(l[1]))):
            c+=1
print(c)