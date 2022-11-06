import math
from decimal import Decimal
class Point:
    def __init__(self , x, y):
        self.x = x
        self.y =y
    def distance(self1 , self2) :      
        hoanh = self1.x - self2.x
        tung = self1.y-self2.y
        hoanh = hoanh*hoanh
        tung = tung*tung
        kq = math.sqrt(hoanh+tung)
        return "{:.4f}".format(kq)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1