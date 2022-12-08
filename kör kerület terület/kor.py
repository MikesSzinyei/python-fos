from area import Area
from perimeter import Perimeter

class Kor():

    def __init__(self):

        self.area=0
        self.perimeter=0
        self.radius=0
        self.choose=0

    def getData(self):

        self.radius=float(input("Sugár: "))

    def calcArea(self):

        self.area=Area().getArea(self.radius)
        print("A kör területe: {:.3} cm2".format(self.area))

    def calcPerimeter(self):

        self.perimeter=Perimeter().getPerimeter(self.radius)
        print("A kör kerülete: {:.3} cm2".format(self.perimeter))
    
    def Chooser(self):

        print("Kerület[1] Terület[2]")
        self.choose=int(input("Válassz: "))

        if self.choose==1:
            self.getData()
            self.calcPerimeter()

        elif self.choose==2:
            self.getData()
            self.calcArea()
        
        else:
            print("[1] vagy [2]!")
            self.Chooser()









kor=Kor()
kor.Chooser()
