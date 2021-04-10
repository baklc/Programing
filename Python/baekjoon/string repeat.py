c=int(input())
for l in range(c):
    n,s=input().split()
    t=""
    for i in s:
        for k in range(int(n)):
            t+=i
    print(t)