t = int(input())
for i in range(t) :
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    k = k % n
    for i in range(k , n ): print(a[i], end = " ")
    for i in range(0, k): print(a[i], end = " ")
    print()