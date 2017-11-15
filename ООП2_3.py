class Сircle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_radius(self,r):
       self.__r = r
       radius=property(set_r,3)
    def __eq__(self, other):
        return self.r == other.r
    def __ne__(self, other):
        return self.r != other.r
    def __lt__(self, other):
        return self.r < other.r
Kryg=Сircle(3,2)
Kryg.radius=5
print(Kryg.radius)
