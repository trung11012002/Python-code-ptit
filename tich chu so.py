t = int(input())
for i in range(t) :
    n = input()
    tich = 1
    for j in n :
        if j != '0' : tich*=int(j)
    print(tich)