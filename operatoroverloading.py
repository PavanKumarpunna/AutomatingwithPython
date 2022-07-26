def add(x,y):
    print(x+y)

add(5,10)
add("Hi","Hello")
add(10.5,3.14)
add(10,5.987)

def add (x,y,z):
    print(x+y+z)

def add(datatype,x,y):
    if datatype == "int":
        #ans = 0
        print(x+y)
    if datatype == "str":
        #ans = ''
        print(str(x)+str(y))
add("str",5,6)