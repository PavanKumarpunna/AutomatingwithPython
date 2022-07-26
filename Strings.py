a = "Hello World"
b = 'Hello World'
print(type(a))
print(type(b))


para = """This a multiline
string example
and it can be inside
3 double or single quotes"""
print(para)

print(len(para))

##########################
#indexing
a = "Hello"
print(a[0])
print(a[-5])

print(a[-2])

#Sciling
print(a[1:4])
print(a[-4:-2])
e = a[-4:-2]
print(e)
print(a[:3])
print(a[2:])
print(a[-4:])

h = "                Hi How   are    you    doing          "
print(h.strip())
print(len(h))
print(len(h.strip()))
print(h.lstrip())
print(h.rstrip())
print(h.lower())
print(h.upper())
i = 'i am an indian'
print(i.capitalize()) # first letter alone it will be captializeed
print(i.title()) #Sentence case
print(i.casefold()) #converts to lower
firstString = "der Fluß"
print(firstString.casefold())
print(firstString.lower())

we =i.replace('i am', 'We are')
print(we)
i = 'i am an indian'
spl = i.split(' ')
print(type(spl))
print(spl[2])
print(i.split('a'))

m = 'malayalam'
print(m.split('a'))

for mal in m:
    print(mal)

if "mal" in "malayalam":
    print('True')

a= 'hi'
b = 'hello'
c= 5
#print(a+b+c)
print(a,b,c)
print(a+b+str(c))
print(a+b+format(c))

a = "I\'am \ran \"Indian\""
print(a)

a = "Hello.. I am Hello"
print(a.count("l"))
print(a.expandtabs(3))

# specify to translate chars
str1 = "wy"

# specify to replace with
str2 = "gf"
trg = "weeksyourweeks"
table = trg.maketrans(str1, str2)
print (trg.translate(table))
print(trg.replace('w','g'))

q = "010"
print(q.zfill(10))