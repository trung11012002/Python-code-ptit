import math
def check (n):
    flag = 1
    if n < 2:
        flag = 0
        return flag
    for p in range(2,(int)(math.sqrt(n))+1):
        if n%p == 0:
            flag = 0
            break
    return flag
t=int(input())
while t > 0 :
    n=int(input())
    if check(n) == 1:
        print("YES")
    else:
        print("NO")
    t-=1