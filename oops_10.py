import math 
class circle :
    def __init__(self,radius):
        self.redius=radius
        self.area=math.pi*self.redius**2

    def display_area(self):
        print(self.area)

class square:
    def __init__(self,side):
        self.side=side
        self.area=self.side**2
    def display_area(self):

C1=circle(10)
C1=display_area()

S1=square(10)
S1=        
        