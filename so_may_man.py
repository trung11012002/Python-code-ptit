t=int(input())
while t > 0:
    s=input()
    tong=0
    ok = True
    for i in s:
        if i != '4' and i != '7':
            ok = False
            break
    if ok :
        print("YES")
    else :
        print("NO")
    t-=1