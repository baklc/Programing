m="""Yh9/=-^:86/f87Y?]-@L}<_E|*1/=-Xi!"Hx865C|-}:|*DL*G_i86/f868FX(@g@-Lh|)=D}_93@_18@g9,*3YC$(@P"""
c=0
file = open("split4_C","w")

d = ""
for i in m:
    d+=i
    c +=1
    if c%4==0:
        print(c)
        file.write(d+"\n")
        d = ""