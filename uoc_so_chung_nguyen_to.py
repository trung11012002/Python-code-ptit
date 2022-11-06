import math
def nguyen_to(n) :
    if n < 2 :
        return False
    for i in range(2,(int)(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True
t = int(input())
while t > 0 :
    a , b = [int(x) for x in input().split()]
    c = math.gcd(a , b)
    d = str(c)
    tong = 0
    for i in d :
        tong+=int(i)
    if nguyen_to(tong) == 1 :
        print("YES")
    else :
        print("NO")
    t-=1
