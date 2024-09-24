def class_D(a1,b1,c1,d1):
    n = int(math.pow(2,32-mask))
    d1 = int(d1/n)*n+ip
    while d1 > 255 :
        c1 = c1 + int(d1/256)
        d1 = d1 - 256
        while c1 > 255:
            b1 = b1 + int(c1/256)
            c1 = c1 - 256
            while c1 > 255:
                a1 = a1 + int(b1/256)
                b1 = b1 - 256
    m = int(256-n)
    netmask = ("255.255.255."+str(m))
    ans = (str(a1)+'.'+str(b1)+'.'+str(c1)+'.'+str(d1)+" "+netmask)
    return(ans)
import math
a,b,c,d = map(int,input().split('.'))
print(a,b,c,d)
mask = int(input('/'))
#p = input('切第幾段：')
#o = input('取第幾段：')
ip = int(input('第幾個可用IP：'))

if mask >= 24:
    print(class_D(a,b,c,d))
