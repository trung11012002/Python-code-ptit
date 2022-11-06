t = int(input())
for k in range(t) :
    s=input()
    ok=1
    tong = 0
    for i in range(len(s) - 1) :
        if abs((int)(s[i]) - (int)(s[i+1])) != 2 :
            ok=0
            break
        tong+=(int)(s[i])
    tong+=(int)(s[len(s) -1])
    if ok == 1 and tong % 10 == 0 :
        print("YES")
    else : print("NO")
