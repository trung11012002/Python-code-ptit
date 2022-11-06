from posixpath import split


a , k , n = [int(x) for x in input().split()]
b = k - a%k + a
ok =False
for i in range(b , n+ 1 ,k) :
    ok = True
    print(i-a , end=" ")
if ok == False :
    print("-1")
    
