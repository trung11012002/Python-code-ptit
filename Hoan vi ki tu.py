ll = input()
nn = len(ll)
x = [0]*(nn+1)
a = [0]*(nn+1)
def Try(i) :
    for j in range(1 , nn+1) :
        if x[j] == 0 :
            x[j] = 1
            a[i] = j
            if i == nn :
                for k in range(1, nn+1) :
                    print(ll[a[k]-1] , end="")
                print()
            else :
                Try(i+1)
            x[j] = 0
Try(1)

        


