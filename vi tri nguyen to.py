import math
def ng_to(n) :
    if n < 2 : return  False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
def check(n) :
    for i in range(len(n)) :
        if ng_to(i) :
            if ng_to(int(n[i])) == False : return False
        else :
            if ng_to(int(n[i])) == True : return False
    return True
t = int(input())
for i in range(t) :
    n = input()
    if check(n) : print("YES")
    else : print("NO")