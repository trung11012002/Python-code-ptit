import math
def ng_to(n) :
    if n < 2 : return  False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    tong = 0
    for j in n :
        tong += int(j)
    s = str(tong)
    if s == s[::-1] and len(s) > 1: print("YES")
    else : print("NO")