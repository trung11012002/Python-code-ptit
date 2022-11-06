
t = int(input())
for i in range(t) :
    n = input()
    tong = 0
    tich = 1
    ok = 0
    for j in range(len(n)) :
        if j % 2 == 1 : tong+=int(n[j])
        else :
            if n[j] != '0' :
                ok=1
                tich*=int(n[j])
    if ok == 0 : print("0" , end = " ")
    else : print(tich , end=" ")
    print(tong)
