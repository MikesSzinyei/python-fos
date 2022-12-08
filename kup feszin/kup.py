from rest03 import Rest03
from rest02 import Rest02
from rest01 import Rest01


class Kup:

    def __init__(self):

        self.surf=0
        self.rest01=0
        self.rest02=0
        self.rest03=0
        self.radius=0
        self.height=0

    def getData(self):

        self.radius=float(input("Sugár: "))
        self.height=float(input("Magasság: "))

    def getResult03(self):

        self.rest03=Rest03().getSqrtResult(self.radius, self.height)

    def getResult02(self):

        self.rest02=Rest02().getMultipleResult(self.radius, self.rest03)


    def getResult01(self):

        self.rest01=Rest01().getPiResult(self.radius)
    
    def calcSurface(self):

        self.surf=self.rest01+self.rest02

        print("A kúp felszíne: {:10.3f}".format(self.surf))

kup=Kup()
kup.getData()
kup.getResult03()
kup.getResult02()
kup.getResult01()
kup.calcSurface()
