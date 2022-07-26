a = "India"
b = 'India'

if a is b: #or a==b
    print("Both are equal")

p = 15
q = 50

if p>q:
    print("True")
    print("1")
    print(2)
print(5)

#if else
p = 15
q = 5

if p<q:
    print('P is lesser')
else:
    print('Q is lesser')

#else if  - elif

x = 10
y = 15
z = 80

if (x>y) and (x>z): #F and T
    print('X is greater--->',x)
elif y>x and y>z: # T and T
    print('Y is greater--->',y)
#elif z>x and z>y: # F and F
else:
    print('Z is greater--->',z)
    print(z,'>',x, 'and',y)
