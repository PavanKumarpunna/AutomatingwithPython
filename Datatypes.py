#Datatypes

#Numbers - int, float and complex
#String
#list
#Tuple
#Set
#Dictionary

a = 10
print(type(a))

f = 10.05
print(type(f))

c = 1+3j
print(type(c))

s = 'sourav'
#str = "Sachin"
print(type(s))
#print(type(str))

i = 89715486456168756321564651648669768973549846867797
print(i)
f = 89.715486456168756321564651648669768973549846867797
print(f)

#isinstance
print(isinstance(i,int)) #i is int or not- true
print(isinstance(i,str)) #i is string or not - false

#Type conversion
pi = 3.14
intpi = int(pi)
print(intpi)

f = 78.99999999999999999999999999
print(f)
print(int(f))

st = "10"
print(int(st))

del st
print(st)
''' #multiline
str = "10a"
print(int(str))
'''


