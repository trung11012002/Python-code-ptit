t = int(input())
for i in range(t) :
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    ok = 1
    for i in range(n) :
        if a[i] > b[i] : ok = 0
    if ok == 1 : print("YES")
    else : print("NO")
