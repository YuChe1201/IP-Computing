import math
a,b,c,d = map(int,input().split('.'))
print(a,b,c,d)
mask = int(input('/'))
#p = input('切第幾段：')
#o = input('取第幾段：')
#ip = input('第幾個IP：')
if mask >= 24:
    n = int(math.pow(2,32-mask))
    print(n)
