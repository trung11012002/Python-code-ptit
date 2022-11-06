import math
f = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
t = int(input())
for i in range(t) :
    n = int(input())
    s = input()
    n = math.log(n, 2)
    n = int(n)
    while len(s) % n != 0 :
        s = '0' + s
    for j in range(0 , len(s), n) :
        sum = 0
        for k in range(j , j+n) :
            if s[k] == '1' : sum+= pow(2,n - k + j -1)
        print(f[sum] , end= "")
    print()
