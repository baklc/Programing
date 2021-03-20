
f = open("97.txt", "r")
bx, by = map(int, f.readline().split())
print(bx, by)
d = []
for i in range(bx):
    d.append([])
    for j in range(by):
        d[i].append(0)
n = int(f.readline())
for i in range(n):
    l,des,x,y = map(int, f.readline().split())
    x = x-1
    y = y-1
    print(l,des,x,y)

    if des == 0:
        for k in range(l):
            if y+k <= by:
                d[x][y+k] = 1
            else:
                break
    if des == 1:
        for k in range(l):
            if x+k <= bx:
                d[x+k][y] = 1
            else:
                break

f.close()

for i in d:
    for j in i:
        print(j, end=" ")
    print()
