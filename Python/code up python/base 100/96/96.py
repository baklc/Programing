a = open("96-1.txt", "r")
d = []
for i in range(19):
    b = list(map(int, (a.readline().split())))
    d.append(b)
n = int(a.readline())
for i in range(n):
    x,y = map(int, a.readline().split())
    x = x-1
    y = y-1
    print(x,y)
    for j in range(19):
        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0







for i in d:
    for j in i:
        print(j, end=" ")
    print()


a.close()