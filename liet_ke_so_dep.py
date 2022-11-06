
t = int(input())
while t > 0 :
    n = int(input())
    ok=1
    for i in range(22,n,2) :
        bien = i 
        s = str(i)
        if len(s) % 2 == 1 or s != s[::-1] :
            ok = 0
        if ok != 0 :
            for j in range(len(s)) :
                k = int(s[j])
                if k % 2 == 1:
                    ok=0
                    break
        if(ok == 1) :
            print(bien, end=" ")
        ok=1
    print()
    t-=1