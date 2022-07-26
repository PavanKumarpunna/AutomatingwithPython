#Set is unordered and its mutable
#It wont allow any duplicates

countryset = {"India","UK","USA","UAE","AUS","India"}
print(countryset)

#indexing, slicing wont work
for c in countryset:
    print(c)

print(len(countryset))

#add - very similar to append
countryset.add("NZ")
print(countryset)

#pop
countryset.pop()
print(countryset)

#remove
countryset.remove("India")
print(countryset)

#discard
countryset.discard("Pak")
print(countryset)

#copy
newcountry = countryset.copy()
print(newcountry)

#clear
#newcountry.clear()
print(newcountry)

#Union
fruits = {"Apple","Banana","Orange","Mango"}
companies = {"Apple","Orange","Google","Facebook"}
print(fruits.union(companies))

#intersection
print(fruits.intersection(companies))

#symmetric diff
print(fruits.symmetric_difference(companies))

print(companies.isdisjoint(fruits))
#differ
print(fruits.difference(companies))
print(companies.difference_update(fruits))
print(companies)

print(companies.isdisjoint(fruits))

supercompanies = {"Apple","Orange","Google","Facebook"}
subcompanies = {'Facebook', 'Google'}

print(supercompanies.issuperset(subcompanies))

print(subcompanies.issubset(supercompanies))

print(supercompanies.update(countryset))
print(supercompanies)