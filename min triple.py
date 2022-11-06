
t = int(input())
while t > 0: 
    n = int(input())
    d = [int(x) for x in input().split()]
    a = 10*8
    b = 10*8
    c = 10**8+1
    for i in range(n) :
        if d[i] < a :
            c = b
            b = a
            a = d[i]
        elif d[i] < b :
            c = b
            b = d[i]
        elif d[i] < c :
            c = d[i]
    print((a+b+c))
    t-=1
