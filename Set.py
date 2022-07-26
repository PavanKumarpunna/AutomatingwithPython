#It wont allow duplicates
#It is unordered

country = {'Ind', 'US', 'UK', 'Aus', 'UAE', 'SA', 'Ind', 'US', 'UK', 'Aus', 'UAE', 'Ind', 'Ind'}
print (country)


for c in country:
    print(c)

country.add("NZ")
print(country)

country.add("NZ")
print(country)

newcountry = country.copy()
print(newcountry)
print(type(newcountry))

newcountry.clear()
print(newcountry)

newco = {} #empty dict
print(type(newco))

newset = set() #empty set
print(type(newset))

company = {"Google","Microsoft","Apple","Orange"}
fruits = {"Apple","Mango","Orange","Grapes"}
#union
print(company.union(fruits))

#Intersection
print(company.intersection(fruits))
'''
company.intersection_update(fruits)
print(company)

newcompany = company.union(fruits)
print(newcompany)
'''

#difference
print(company.difference(fruits))

#symmetric Diff
print(company.symmetric_difference(fruits))

#Discard - its will not throw you any error
company = {"Google","Microsoft","Apple","Orange"}
company.discard("Facebook")
print(company)
company.discard("Google")
print(company)

#remove - it will throw error, if we dont hav value
company = {"Google","Microsoft","Apple","Orange"}

company.discard("Google")
print(company)
#company.remove("Facebook")
#print(company)


company = {"Google","Microsoft","Apple","Orange"}
fruits = {"Apple","Mango","Orange","Grapes"}
print(company.isdisjoint(fruits))
print(country.isdisjoint(fruits))

fruits = {"Apple","Mango","Orange","Grapes"}
Comp = {"Apple","Orange"}
print(fruits.issubset(Comp))
print(Comp.issubset(fruits))


fruits = {"Apple","Mango","Orange","Grapes"}
Comp = {"Apple","Orange"}
print(fruits.issuperset(Comp))
print(Comp.issuperset(fruits))

print(fruits.pop())
print(fruits)