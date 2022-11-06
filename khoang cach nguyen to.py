from array import array

a = [1]*(1000001)

def sang() :
    a[0] = a[1] = 0
    for i in range(2,10001) :
        if a[i] == 1 :
            for j in range(i*i , 1000001,i) :
                a[j] = 0
sang()
x = []
for i in range(1,1000001) :
    if a[i] == 1 :
        x.append(i)

n , k = [int(x) for x in input().split()]
print(k , end = " ")
for i in range(n):
    print(k+x[i] ,  end = " ")
    k = k + x[i]

