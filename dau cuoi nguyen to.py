import math
def ng_to(n) :
    if n < 2 : return  False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    s1 = n[-3::]
    s2 = n[:3]
    if ng_to(int(s1)) and ng_to(int(s2)) : print("YES")
    else : print("NO")
