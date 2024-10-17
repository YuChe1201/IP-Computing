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
def class_D_3(a1,b1,c1,d1):
    n = int(math.pow(2,32-mask))
    if n > p:
        j = n/p
        d1 = int(int(d1/n)*n+int(o-1)*j+ip)
    a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
    m = int(256-j)
    netmask = ("255.255.255."+str(m))
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
def class_C_3(a1,b1,c1,d1):
    n = int(math.pow(2,24-mask))
    if n > p:
        j = n/p
        c1 = int(int(c1/n)*n+int(o-1)*j)
        d1 = ip
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-j)
        netmask = ("255.255."+str(m)+".0")
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
    elif n < p:
        j = p/n
        j2 = int(o/j)
        i = int(256/j)
        c1 = int(c1/n)*n+j2
        d1 = int((o%j-1)*i+ip)
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-i)
        netmask = ("255.255.255."+str(m))
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
def class_B_3(a1,b1,c1,d1):
    n = int(math.pow(2,16-mask))
    if n > p:
        j = n/p
        b1 = int(int(b1/n)*n+int(o-1)*j)
        d1 = ip
        c1 = 0
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-j)
        netmask = ("255."+str(m)+".0.0")
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
    elif n < p:
        j = p/n
        j2 = int(o/j)
        i = int(256/j)
        b1 = int(b1/n)*n+j2
        c1 = int((o%j-1)*i)
        d1 = ip
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-i)
        netmask = ("255.255."+str(m)+".0")
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
def class_A_3(a1,b1,c1,d1):
    n = int(math.pow(2,8-mask))
    if n > p:
        j = n/p
        a1 = int(int(a1/n)*n+int(o-1)*j)
        d1 = ip
        c1 = 0
        b1 = 0
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-j)
        netmask = (str(m)+".0.0.0")
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
    elif n < p:
        j = p/n
        j2 = int(o/j)
        i = int(256/j)
        a1 = int(a1/n)*n+j2
        b1 = int((o%j-1)*i)
        d1 = ip
        c1 = 0
        a1,b1,c1,d1 = Carry(a1,b1,c1,d1)
        m = int(256-i)
        netmask = ("255."+str(m)+".0.0")
        ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
        return(ans)
import math
a,b,c,d = map(int,input().split('.'))
mask = int(input('/'))
p = int(input('切第幾段：'))
o = int(input('取第幾段：'))
ip = int(input('第幾個可用IP：'))

if mask >= 24:
    print(class_D_3(a,b,c,d))
elif mask >= 16:
    print(class_C_3(a,b,c,d))
elif mask >= 8:
    print(class_B_3(a,b,c,d))
elif mask >= 0:
    print(class_A_3(a,b,c,d))