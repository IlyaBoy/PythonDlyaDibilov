class String_saver:
    def getS(self):
       return self.__S*3
    def setS(self, value):
       self.__S = value
    def delS(self):
       del self.__S
    S = property(getS, setS, delS, "String")

Str=String_saver()
Str.S="улизорил"
print(Str.S)
del Str.S
