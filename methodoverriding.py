class rectangle():
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        print(self.length*self.breadth,"is area of rectangle")

    def printrect(self):
        print("This is a rectangle")

class square(rectangle):
    def __init__(self,side):
        self.side = side
    def getArea(self):
        print(self.side**2,"is area of square")

    def printarea(self):
        print("This is an area")

s = square(4)
s.getArea()
s.printarea()
s.printrect()

r = rectangle(5,10)
r.getArea()