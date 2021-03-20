# -*- coding:utf-8 -*-

import base64

id = "admin"
pw = "nimda"

idt = id.encode()
pwt = pw.encode()

for i in range(20):
    idt = base64.b64encode(idt)
    pwt = base64.b64encode(pwt)

idt = idt.decode()
pwt = pwt.decode()
print(idt,pwt, end="\n")

intab = "12345678"
outtab = "!@$^&*()"

trantab = idt.maketrans(intab, outtab)

print("\n" + idt.translate(trantab) + "\n" + pwt.translate(trantab))
