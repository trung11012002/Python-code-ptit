import math
def ng_to(n) :
    if n < 2 : return  False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
def check(n) :
    for i in range(len(n)) :
        if i % 2 == 0 :
            if int(n[i]) % 2 == 1 : return False
        else :
            if int(n[i]) % 2 == 0 : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    tong  = 0
    for j in n : tong += int(j)
    if ng_to(tong) and check(n) : print("YES")
    else : print("NO")
