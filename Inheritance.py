#Animal - with some functions
#Dog  -
#Cat

class animal:
    def eat(self):
        print("Animal will be eating")

    def sleep(self):
        print("Animal will be sleeping")


class dog (animal):

    def usedfor(self):
        print("Dogs are used to protect houses")

class bulldog(dog):
    def protect(self):
        print("used to attack strangers")



class cat(animal):

    def chaserat(self):
        print("cats are used to chase rats")



a = animal()
a.sleep()
a.eat()

d = dog()
d.sleep()
d.eat()
d.usedfor()
#a.chaserat()

b = bulldog()
b.sleep()
b.eat()
b.usedfor()
b.protect()