class Сircle:
    def __init__(self,r=1,x=0,y=0):
        self.x=x
        self.y=y
        self.r=abs(r)

    def __eq__(self, other):
        return self.r == other.r
    def __ne__(self, other):
        return self.r != other.r
    def __lt__(self, other):
        return self.r < other.r

C1=Сircle(12,0,0)
C2=Сircle(11,3,5)
if C1>C2:
    print('C1>C2')
elif C1<C2:
    print('C1<C2')
elif C1==C2:
    print('C1=C2')
