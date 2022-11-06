
n , k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
a.append('1')
ll = []
for i in range(len(a)-1) :
    if a[i] != a[i+1] :  ll.append(a[i])
n = len(ll)


b = [0] * (k+1)
def Try(i) :
    for j in range(b[i-1] + 1 , n-k+i+1) :
        b[i] = j
        if i == k :
            for z in range(1 , k+1) :
                print(ll[b[z] - 1] , end = " ")
            print()
        else : Try(i+1)
Try(1)


