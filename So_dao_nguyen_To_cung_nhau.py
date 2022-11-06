from ast import Str
from math import gcd


t= int(input())
while t > 0 :
    s = input()
    ss = s[::-1]
    m = gcd(int(s),int(ss))
    if m == 1 :
        print("YES")
    else :
        print("NO")
    t-=1