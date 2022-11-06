t = int(input())
while t > 0 :
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    ok = 1
    for i in range(len(a)) :
        if a[i] > b[i] :
            ok = 0
            break
    if ok == 1 : print("YES")
    else : print("NO")
    t -=1