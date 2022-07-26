class room:
    def __init__(self):
        self.length = 10
        self.breadth = 15
        self.cost = 200

    def area(self):
        return self.length*self.breadth

    def calcost(self):
        area = self.area()
        print(area)
        #print(self.cost())
        return area * self.cost

class circle(room):
    def area(self):
        #self.cost = cost
        #print(self.cost)
        return room.length*room.length

class square(room):
    def area(self):
        return self.length*self.length
############################################
livingroom = room()
print(livingroom.area())
print(type(livingroom.area()))
print(livingroom.calcost())
print(livingroom.cost)


############################################
kitchen = room()
print("Kitchen Area",kitchen.area())
print(type(kitchen.area()))
print("Cost of furnishing",kitchen.calcost())

###############################################

c = circle()
print(circle.area)
print(circle.calcost)