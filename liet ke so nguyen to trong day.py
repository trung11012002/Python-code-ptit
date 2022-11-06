a = [1]*(1000001)

def sang() :
    a[0] = a[1] = 0
    for i in range(2,10001) :
        if a[i] == 1 :
            for j in range(i*i , 1000001,i) :
                a[j] = 0
sang()
n=int(input())
b = [int(x) for x in input().split()]
c = [0]*1000001
for i in b :
    if a[i] == 1 :
        c[i] +=1
for i in b :
    if c[i] >= 1 :
        print(i , " " , c[i]) 
        c[i] = 0
 
