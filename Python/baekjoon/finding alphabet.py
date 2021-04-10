a=list(input())
l=[]
for i in range(26):
    l.append(-1)
for i in range(97,123):
    if chr(i) in a:
        l[i-97]=a.index(chr(i))
for k in l:
    print(k,end=" ")