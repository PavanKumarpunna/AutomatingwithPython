import math
import time

from Selenium_Vijay.Calc_Function import subtraction as sub
time.sleep(3)


a = 100
b = 50
c  = 10
d = 5
x = 7
y = 4


print(sum(a,y))
print(sub(d,x))
print(sum(a,b)*sub(c,d)/mul(x,y)*div(7,5)+power(50,3))


def coffee(x,y,z):

    """
    :param x: To add milk
    :param y: To add Coffee powder
    :param z: To add hot water
    :return: coffee
    """

    if x != "null":
        return "milk"

    if y!= "null":
        return "coffee powder"

    if z!= "null":
        return "hotwater"

    else:
        return "milk + coffee powder"


print(coffee("null","null","null"))

print(math.factorial(4))

def fact(num):
    if num <= 0:
        return "Enter greater than 0"
    elif num == 1:
        return 1
    else:
        return (num* (fact(num-1)))

print(fact(10))

