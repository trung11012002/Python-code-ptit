p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True :
    ip = input()
    if ip == "0" : break
    k , s = ip.split()
    ss=""
    for i in range(len(s)) :
        x = 0
        for j in p :
            if s[i] == j :
                break
            x+=1
        x = (x+int(k)) % 28
        ss = ss + p[x]
    print(ss[::-1])
    