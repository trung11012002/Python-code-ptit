from curses.ascii import isdigit


t = int(input())
while t > 0:
    s = input()
    sum = 0
    res =""
    for c in s:
        if c.isdigit():
            sum+=int(c)
        else :
            res+=c
    print("".join(sorted(res)) + str(sum))
    t-=1