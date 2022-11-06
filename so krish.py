def gt(n) :
    sum = 1
    while n > 0 :
        sum*= n
        n-=1
    return sum
t = int(input())
while t > 0 :
    n = input()
    sum = 0
    for i in n :
        sum+= gt(int(i))
    if sum == int(n) : print("Yes")
    else : print("No")
    t-=1