import math
def check(n) :
    for i in range(2,(int)(math.sqrt(n)+1)) :
        dem = 0
        if n % i == 0 :
           
            while n % i == 0 :
                dem+=1
                n/=i
            print(" * " + str(i) + "^" + str(dem) ,end="")
    if n != 1 :
        n=(int)(n)
        print(" * " + str(n) + "^1" ,end = "")

t = int(input())
for k in range(t) :
    n = int(input())
    print("1" , end="")
    check(n)
    print()
    