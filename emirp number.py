import math


def ngTo(n) :
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    for i in range(1,n) :
        s1 = str(i)
        s2 = s1[::-1]
        if int(s1) < int(s2) and int(s2) < n:
            if ngTo(int(s1)) and ngTo(int(s2)) : print(s1,s2, end = " ")
    print()