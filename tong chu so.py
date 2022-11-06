# def trans(s) :
#     n = 0
#     for i in s : n += ord(i) - ord('0')
#     return str(n)

n = input()
count = 0
while len(n) > 1:  
    sum = 0
    for i in n :
        sum += (ord(i) - ord('0'))
    n = str(sum)
    count +=1
print(count)