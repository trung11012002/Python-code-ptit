import math
def ng_to(n) :
    if n < 2 : return  False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    k = int(n[-4::])
    if ng_to(k) : print("YES")
    else : print("NO")