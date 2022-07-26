#operators - performing operations on variables

#Arithmetic
a = 10 #Assignment Operator
b = 6

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a//b) #Quoient value
print(a%b) #remainder value
print(a**b) #power

#Comparison
a = "India"
b = 'India'

print(a == b)
print(a != b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#Assignment
a = 10

a +=10
print(a)
a -= 10
print(a)
a *=10
print(a)
a /=10
print(a)
a //=10
print(a)
a%=10
print(a)
a**=10
print(a)

a = 10
b = 5
c = 50
if a*b == c and 10*5 == 50:
    print('its 50')


if a*b == c or 10*4 == 50:
    print('it can be 50')


#in operatpor - membership
#contains

FullString = "Its a sunday"
subStr = "sun"

if subStr in FullString:
    print("Yes")

if "sun" in "Its a sunday":
    print("Yes")

