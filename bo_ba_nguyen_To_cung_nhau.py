from math import gcd
a , b =[int(x) for x in input().split()]
for i in range(a , b + 1 - 2) :
    for j in range(i+1 , b+1 - 1) :
        if gcd(i,j) == 1 :          
            for k in range(j+1,b+1) :
                if gcd(i,k) == 1 and gcd(j,k) == 1  :
                    print("(" + str(i) + ", " + str(j) +", " + str(k) + ")")