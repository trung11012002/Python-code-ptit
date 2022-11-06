from cmath import sqrt
import math
def ng_to(n) :
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    k = len(n)
    so_nguyen_to = 0
    so_ko_nguyen_to = 0
    for j in n :
        if ng_to(int(j)) : so_nguyen_to +=1
        else : so_ko_nguyen_to +=1
    if ng_to(k) and so_nguyen_to > so_ko_nguyen_to :
        print("YES")
    else :
        print("NO")
