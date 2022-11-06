t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    b = {}
    max  = 0
    value = 0
    for i in a :
        if i in b :
            b[i] +=1
        else : b[i] = 1
    for i in a :
        if max < b[i] :
            max = b[i]
            value = i
    if max > n/2 : print(value)
    else : print("NO")
    t-=1