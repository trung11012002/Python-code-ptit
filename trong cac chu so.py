
t = int(input())
while t > 0 :
    s = input()
    sum = 0
    kq = ""
    for i in s :
        if i.isdigit() : sum += int(i)
        else : kq += i
    kq = ''.join(sorted(kq))
    print(kq + str(sum))
    t-=1