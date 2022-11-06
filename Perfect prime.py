import math


def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

def check(s) :
    for i in s :
        if nto(int(i)) == False  : return False
    return True

t = int(input())
for i in range(t) :
    n = int(input())
    nn = int(str(n)[::-1])
    s  =str(n)
    sum = 0
    for i in s :
        sum += int(i)
    if check(s) and nto(n) and nto(nn) and nto(sum) :
        print("Yes")
    else : print("No")
