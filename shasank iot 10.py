# Area of circle using oops
import math

class rect:
    def __init__(self,L,B):
       self.L = 6
       self.B = 5
       
    def arearect(self):
        return self.L*self.B

# Driver code

t=rect(6,5)

a=t.arearect()

print("area of rect",a)
