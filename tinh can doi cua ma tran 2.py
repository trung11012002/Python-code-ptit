n  = int(input())
a = [[]] * n
for i in range(n) :
    a[i] = [int(x) for x in input().split()]
k = int(input())

ss1 = 0
ss2 = 0
for i in range(n) :
    for j in range(n) :
        if  i < j : ss1+=a[i][j]
        elif j < i : ss2+= a[i][j]
s = abs(ss1-ss2)
s1 = 0
s2 = 0
for i in range(n) :
    for j in range(n) :
        if j < n-i-1 : s1 += a[i][j]
        elif j > n - i - 1: s2+= a[i][j]
ss = abs(s1-s2)
kq = abs(ss-s)
if kq <= k :
    print("YES")
else : print("NO")
print(kq)