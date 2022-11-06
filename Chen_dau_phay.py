s = input()
dem = 0
x=""
for i in range(0,len(s)) :
    dem+=1
    x = x + s[-i-1]
    if dem == 3 and i != len(s)-1:
        x = x + ","
        dem=0
print(x[::-1])
