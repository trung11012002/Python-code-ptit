t = int(input())
while t > 0 :
    n = int(input())
    while n % 7 != 0 :
        s = str(n)
        ss = s[::-1]
        n = int(s) + int(ss)
    print(n)
    t-=1