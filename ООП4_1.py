import math

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.normal=math.sqrt(x*x+y*y)

    def print_point(self):
        print('Point: x = '+str(self.x)+'; y = '+str(self.y))

    def __eq__(self, other):
        return self.normal == other.normal
    def __ne__(self, other):
        return self.normal != other.normal
    def __lt__(self, other):
        return self.normal < other.normal

    def __add__(self, other):
        return(Point(self.x+other.x,self.y+other.y))

P1=Point(2,3)
P2=Point(3,5)
P3=P1+P2
P3.print_point()
