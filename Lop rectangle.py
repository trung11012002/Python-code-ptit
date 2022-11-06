class Rectangle :
    def __init__(self , dai , rong , color) :
        self.dai = dai
        self.rong = rong
        self.colorr = color[0:1].upper() + color[1:].lower()
    def perimeter(self) :
        return str((self.dai+self.rong)*2)
    def area(self) :
        return str(self.dai*self.rong)
    def color(self) :
        return str(self.colorr)
if __name__ == '__main__':
    arr = input().split() 
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color())) 
    else: print('INVALID')