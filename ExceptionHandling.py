'''

try - test a block of code of errors
except - handle the error
finally - regardless of error its going to execute

'''
import os


def divide(x,y):
    try:
        print (x//y)
    except:
        print("Dividing by zero is not possible")
divide(10,2)
print("Hello world")

try:
    #p = 5
    print(10//0)
except NameError:
    print("P is not declared")
except ZeroDivisionError:
    print("division by zero is not possible")
finally:
    print("This is finally statement")

try:
    f = open("C:\\Users\\Vignesh\\OneDrive\\Desktop\\Exceptions.txt","w")
    f.write("Python demo")
except:
    print("Somethg wrong in writing the file")

finally:
    f.close()


try:
    os.path.exists("C:\\Users\\Vignesh\\OneDrive\\Desktop\\Exceptions.txt")
    os.remove("C:\\Users\\Vignesh\\OneDrive\\Desktop\\Exceptions.txt")
except:
    print("The file doesnot exist")

try:
    os.remove("C:\\Users\\Vignesh\\OneDrive\\Desktop\\Exceptions - Copy.txt")
except:
    print("File not availble")


x = -1
if x < 0:
    raise Exception("Number is less than zero")


y = -5
print(y)