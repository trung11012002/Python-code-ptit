t = int(input())
while t > 0 : 
    n = input()
    s= ""
    ss=""
    for i in range(len(n)) :
        if i % 2 == 0 :
            s+=n[i]
        else :
            ss+=n[i]
    ok = 1
    for i in range(len(s)-1) :
        if s[i] != s[i+1] :
            ok=0
            break
    for i in range(len(ss) - 1) :
        if ss[i] != ss[i+1] :
            ok= 0
            break
    if ok ==1 :
        print("YES")
    else :
        print("NO")
    t-=1