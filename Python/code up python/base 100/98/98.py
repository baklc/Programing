import time
f = open("98-1.txt", "r")
bx, by = 1,1
d = []

for i in range(10):
    a = list(map(int, (f.readline()).split()))
    d.append(a)


x,y = bx, by
while True:
    if d[y][x] == 2:
        break
    if d[y][x] == 1:
        y = y+1
        x = x-1
        if x == 8:
            if y == 8:
                d[y][x] = 9
                break
        if d[y][x] == 2:
            break
        d[y][x] = 9
        x = x+1
    elif d[y][x] == 0:
        d[y][x] = 9
        x = x+1

for i in d:
    for k in i:
        print(k, end=" ")
    print()


