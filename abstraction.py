from abc import ABC, abstractmethod

class absclass(ABC):
    def print (self,x):
        print("Value of x is", x)
    @abstractmethod
    def task(self):
        print("I am inside absclass-task")

class test_class(absclass):
    def task(self):
        print("I am inside test-class task")

class eg_class(absclass):
    def task(self):
        print("I am inside eg-class task")

test_obj = test_class()
test_obj.task()
test_obj.print(15)


#parent = absclass()
#parent.print(5)


class payment(ABC):
    def print_slip(self,amount):
        print("Purchase amount", amount)

    @abstractmethod
    def paymentmethod(self):
        #hide all details
        pass

class CreditCard(payment):
    def paymentmethod(self):
        print("Credit card payment")

class DebitCard(payment):
    def paymentmethod(self):
        print("Debit card payment")

c = CreditCard()
c.paymentmethod()
c.print_slip(1500)

d = DebitCard()