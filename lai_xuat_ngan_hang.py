import math
t = int(input())
while t > 0 :
    n = float(input())
    x = float(input())
    m = float(input())
    x/=100
    a = math.log(m/n , (1+x))
    print(a)
    t-=1