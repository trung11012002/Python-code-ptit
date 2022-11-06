t = int(input())
ok = 1
while t > 0 :
    s1 = input()
    s2 = input()
    s1 =  sorted(s1)
    s2 = sorted(s2)
    if s1 == s2 : print("Test {}: YES".format(ok))
    else : print("Test {}: NO".format(ok))
    ok +=1
    t-=1