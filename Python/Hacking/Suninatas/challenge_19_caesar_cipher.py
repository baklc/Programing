a = input("input")
string_list=['IS', 'THE', 'ARE', 'MOST', 'CONGRATULATION']
all=[]
for c in range(26):

    dd = []
    for i in list(a):
        aa=ord(i)-c
        if aa < 65:
            k=1
        if i == ' ':
            dd.append(' ')
        else:
            if aa<65:
                dd.append(chr(ord(i)-c+26))
            else:
                dd.append(chr(ord(i) - c))

    result= ''.join(dd)
    all.append(result)

for k in all:
    for l in string_list:
        if l in k:
            print(k)