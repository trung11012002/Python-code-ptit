def check1(n) :
    if len(n) % 2 == 1 : return False
    for i in n :
        if int(i) % 2 == 1 : return False
    return True
t = int(input())
for i in range(t) :
    n = int(input())
    for j in range(22,n+1,2) :
        k = str(j)
        if check1(k) == True and k == k[::-1] :
            print(k , end=" ")
    print()
