class employee:

    def __init__(self,name):
        self.name = name

    def hello(self):
        print(self.name)

class subemp(employee):
    def anythng(self):
        print("Hello")


s = subemp("India")
print(s.name)
s.hello()
s.anythng()