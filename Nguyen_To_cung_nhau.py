from math import gcd
n , k = [int(x) for x in input().split()]
a = 10**(k-1)
b = 10**k
ok=0
for i in range(a,b) :
    if  gcd(n,i) == 1:
        print(i , end = " ")
        ok+=1
        if ok % 10 == 0 :
            print()
