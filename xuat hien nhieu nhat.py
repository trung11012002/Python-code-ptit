
from msilib import knownbits


t = int(input())
for i in range(t) :
    n = int(input())
    a = [int(x) for x in input().split()]
    k  = n // 2
    print(k)
    a = sorted(a)
    vt = -1000
    vtt = -1000
    for j in range(n-1) :
        cnt = 1
        for k in range(j+1 , n) :
            if a[k] == a[j] : cnt +=1
        print(cnt)
        if cnt > k and cnt > vt :
            vtt = j
            vt = cnt
    if vtt == -1000 : print("NO")
    else : print(vtt)



