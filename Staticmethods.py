class addition:
    def add(x,y):
        return x+y
'''
a = addition()
print(a.add(5,6))
'''
#addition.add = staticmethod(addition.add)
print(addition.add(5,8))

class multiplication:
    @staticmethod
    def mul(x,y):
        return x*y

print(multiplication.mul(5,6))


class employee:
    def __init__(self,name):
        self.name = name
    @classmethod
    def empname(cls,name):
        print(cls(name))
    @staticmethod
    def emplyname(name):
        return name
e = employee("Virat")
employee.empname("Dhoni")
print(employee.emplyname("Virat"))


class Fruit:
    name = 'Fruits'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit.printName()
