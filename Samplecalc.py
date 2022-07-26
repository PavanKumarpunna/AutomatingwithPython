class summation:
    def sum(self,a,b):
        return a+b

class multiplication:
    def mul(self,a,b):
        return a*b

class Dividenum(summation,multiplication):
    def div(self,a,b):
        return a/b

d = Dividenum()
print(d.sum(5,10))
print(d.mul(5,10))
print(d.div(10,5))