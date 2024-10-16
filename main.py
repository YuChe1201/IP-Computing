def Carry(a1,b1,c1,d1):
    while d1 > 255 :
        c1 = c1 + 1
        d1 = d1 - 256
        while c1 > 255:
            b1 = b1 + 1
            c1 = c1 - 256
            while c1 > 255:
                a1 = a1 + 1
                b1 = b1 - 256
    return a1,b1,c1,d1
def class_D(a1,b1,c1,d1):
    n = int(math.pow(2,32-mask))
    a1,b1,c1,d1 = list(map(int,[a1,b1,c1,d1]))
    d1 = int(d1/n)*n+ip
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255.255.255."+str(m))
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_C(a1,b1,c1,d1):
    n = int(math.pow(2,24-mask))
    a1,b1,c1,d1 = list(map(int,[a1,b1,c1,d1]))
    c1 = int(c1/n)*n
    d1 = ip
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255.255."+str(m)+".0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_B(a1,b1,c1,d1):
    n = int(math.pow(2,16-mask))
    a1,b1,c1,d1 = list(map(int,[a1,b1,c1,d1]))
    b1 = int(b1/n)*n
    d1 = ip
    c1 = 0
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255."+str(m)+".0.0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_A(a1,b1,c1,d1):
    n = int(math.pow(2,8-mask))
    a1,b1,c1,d1 = list(map(int,[a1,b1,c1,d1]))
    a1 = int(a1/n)*n
    d1 = ip
    c1 = 0
    b1 = 0
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = (str(m)+".0.0.0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_D_2(a1,b1,c1,d1):
    n = int(math.pow(2,32-mask))
    a1,b1,c1 = list(map(int,[a1,b1,c1]))
    d1 = int(o-1)*n+ip
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255.255.255."+str(m))
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_C_2(a1,b1,c1,d1):
    n = int(math.pow(2,24-mask))
    a1,b1 = list(map(int,[a1,b1]))
    c1 = int(o-1)*n
    d1 = ip
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255.255."+str(m)+".0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_B_2(a1,b1,c1,d1):
    n = int(math.pow(2,16-mask))
    a1 = int(a1)
    b1 = int(o-1)*n
    d1 = ip
    c1 = 0
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = ("255."+str(m)+".0.0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_A_2(a1,b1,c1,d1):
    n = int(math.pow(2,8-mask))
    a1 = int(o-1)*n
    d1 = ip
    c1 = 0
    b1 = 0
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-n)
    netmask = (str(m)+".0.0.0")
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
import math
a,b,c,d = map(str,input().split('.'))
mask = int(input('/'))
#p = input('切第幾段：')
o = int(input('取第幾段：'))
ip = int(input('第幾個可用IP：'))

if mask >= 24:
    if d == 'x':
        print(class_D_2(a,b,c,d))
    else:print(class_D(a,b,c,d))
elif mask >= 16:
    if c == 'x':
        print(class_C_2(a,b,c,d))
    else:print(class_C(a,b,c,d))
elif mask >= 8:
    if b == 'x':
        print(class_B_2(a,b,c,d))
    else:print(class_B(a,b,c,d))
elif mask >= 0:
    if a == 'x':
        print(class_A_2(a,b,c,d))
    else:print(class_A(a,b,c,d))

