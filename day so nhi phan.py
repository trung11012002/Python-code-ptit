n = int(input())
a = [int(x) for x in input().split()]
s = 0
for i in range(0 , n-1) :
   if a[i] != a[i+1] : s+=1
print(s)
