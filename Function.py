def greeting():
    x = 10
    y = 15
    z = x+y
    print(z)
    return "Hello.. How are you..!!"

#greeting()
print(greeting())

def add (x,y):
    #Python doc
    """This is an add function
    it can add both string,float and int"""
    return x+y

print(add(3,5)+15)
print(add.__doc__)

print(add("Python","Selenium"))
print(add(3.14,4))

print(add("Python",format(3)))

def sqarea(a):
    return a*a
print(sqarea(50))
cost =  sqarea(50) * 75
print(cost)

print ('--------------------------------------')###########
list1 = [1,2,5,1,2,4,6,7,4,7,8,9]
list2 = [5,2,5,11,15,4,16,17,4,17,181,19]
#print(set(list1))

def uniquelist(l):
    #return set(l)
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

uniquelist(list1)
#print(uniquelist(list2))