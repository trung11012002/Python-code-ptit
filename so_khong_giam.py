t=int(input())
while t > 0 :
    s = input()
    ok=1
    for i in range(len(s)-1) :
        if s[i] > s[i+1] :
            ok = 0
    if ok == 1 :
        print("YES")
    else :
        print("NO")
    t-=1