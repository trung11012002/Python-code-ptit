t = int(input())
for i in range(t) :
    a = []
    s = input()
    s = s + " "
    x = ""
    for j in range(len(s)) :
        k = 0
        if s[j] < '0' or s[j] > '9':
            if len(x) > 0 :
                for m in x :
                    k = k*10 + int(m)
                a = a + [k]
                x=""
        else :
            x = x + s[j]
    a = sorted(a)
    if len(a) > 0 : print(a[-1])
    else : print()

        