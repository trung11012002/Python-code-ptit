
import math


while True :
    a = [int(x) for x in input().split()]
    if a.count(0) == 4 :
        break
    ok = 0 
    while a.count(a[0]) != 4 :
        ok+=1
        x = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(x - a[3])
    print(ok)