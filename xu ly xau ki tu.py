a = {str(x).lower() for x in input().split()}
b = {str(x).lower() for x in input().split()}
c = set()
for i in b :
    c.add(i)
for i in a :
    c.add(i)
c = sorted(c)
for i in c :
    print(i , end = " ")
print()
a = sorted(a)
for i in c :
    if i in b and i in a:
        print(i , end = " ")
print()