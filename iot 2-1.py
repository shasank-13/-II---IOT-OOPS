# Area of circle using OOP
import math

class circle:
    def __init__(self, r):
        self.r = r
    
    def calarea(self):
        return math.pi * self.r ** 2
    
    def cirper(self):
        return 2 * math.pi * self.r

# driver code
r = float(input("Input the radius of the circle: "))

a = circle(r)

area = a.calarea()
perimeter = a.cirper()

print("Area of circle:", area)
print("Perimeter of circle:", perimeter)
