a = [0 , 1 , 1]
f1=1
f2=1
for i in range(3,93) : 
    k = f1+f2
    a = a+[k]
    f2 = f1 
    f1 = k
t = int(input())
for i in range(t) :
    l , r = [int(x) for x in input().split()]
    for j in range(l , r+1) :
        print(a[j] , end = " ")
    print()

