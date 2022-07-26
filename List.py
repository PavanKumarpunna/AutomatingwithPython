#List is very similar to Array but we can add/delete data easily
#Its ordered and modifiable

fruits = ["Orange","Apple","Mango","Stawberry"]
print(fruits)
print(type(fruits))

#Indexing
print(fruits[3])
#Negative Indexing
print(fruits[-3])

#slicing
print(fruits[1:3])
newfruits = fruits
print(newfruits)

#Negative Slicing
print(fruits[-4:-2])

fruits = ["Orange","Apple","Mango","Stawberry"]

#For each loop
for f in fruits:
    print(f)

#For loop  range

for i in range(len(fruits)):
    print(fruits[i])

############################################################

#Append will add after Aus
country = ["Ind","US","UK","Aus"]
country.append("UAE")
print(country)

#Clear
print(newfruits)
newfruits.clear()
print(newfruits)

#copy
newcountry = country.copy()
print(newcountry)

#Count
newcountry.append("Ind")
newcountry.append("Ind")
print(newcountry)
print(newcountry.count('Ind'))
print(newcountry.count('Aus'))

pyt = "LearningPythonwithSelenium"  #4
print(pyt.count('n'))
print(pyt.count('z'))

#extend - give list as input
newcountry1 = ["UAE","NZ"]
country.extend(newcountry)
country.extend(newcountry1)
print(country)

#index
print(country.index('UAE'))
print(country.index('NZ'))

#insert
country.insert(5,"SA") #position and value
print(country)

country.insert(5,newcountry1)
print(country)
print(country[5][1])
#Append - it will always insert at the end
#Insert - here we can insert in mentioned position
#Extend - mainly used for extending 2 list

#Pop
# Without index - it will pop out the last value
# with index - it will pop the specified value of that index

print(country.pop())
print(country.pop())
print(country)

print(country.pop(5))
print(country)

#remove
country.remove('UAE')
print(country)

#reverse
country.reverse()
print(country)

#Sort
#country.sort()
#print(country)

country.sort(reverse=True)
print(country)

numlist = [1,5,9,7,4,2,3]
print(numlist)
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)

