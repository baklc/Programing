l=["c=","c-","dz=","d-","lj","nj","s=","z="]
a=input()
c=0
for i in l:
    if a.find(i) != -1:
        n=a.find(i)
        c+=1
        while a[n+1:].find(i) != -1:
            n=a[n+1:].find(i)+n+1
            c+=1
    else:
        pass
    a=a.replace(i," ")
a=a.replace(" ","")
c+=len(a)
print(c)