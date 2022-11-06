import math
t =int(input())
def ng_to(n) :
    if n < 2 : return 0
    for i in range(2,(int)(math.sqrt(n))+1) :
        if n % i == 0 : return 0
    return 1
while t  > 0:
    n = int(input())
    dem = 0
    for i in range(1,n) :
        if math.gcd(n,i) == 1 :
            dem += 1
    if ng_to(dem) == 1 :
        print("YES")
    else :
        print("NO")
    t-=1