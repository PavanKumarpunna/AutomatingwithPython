newdict = {
    "id":195519,
    "name": "Tommy",
    "country":"US",
    "timezone":"EST"

}

print(newdict["id"])

thisdict = {
    1 : "India",
    "fruit":18,
    "vegetable" : "carrot"
}

print(thisdict.get(1))
#print(thisdict[2])

#For loop

#keys
for t in thisdict:
    print(t)

for t in thisdict.keys():
    print(t)

#values
for t in thisdict:
    print(thisdict[t])
    print(thisdict.get(t))

for t in thisdict.values():
    print(t)

#items
for t in thisdict.items():
    print(t)

for t,s in thisdict.items():
    print(t,s)
    if t == 'vegetable':
        veg = 'vegetable'
        break

print(thisdict)


copydict = newdict.copy()
print(copydict)
print(newdict)

copydict.clear()
print(copydict)


#Pop
newdict.pop("name")
print(newdict)

#popitem
newdict.popitem()
print(newdict)

newdict = {
    "id":195519,
    "name": "Tommy",
    "country":"US",
    "timezone":"EST"
}

x = newdict.setdefault("name","Mr. Tom")
print(x)

x = newdict.setdefault("Full name","Mr. Tom")
print(x)
print(newdict)



car = { "brand": "Ford","model": "Mustang","year": 1964}
x = car.setdefault("owner", "Tom")
print(x)
print(car)


newdict = {
    "id":195519,
    "name": "Tommy",
    "country":"US",
    "timezone":"EST",
    "id":2525

}

print(newdict.update({"id":"19555"}))
print(newdict)
print(newdict.update({"divid":"HR01"}))
print(newdict)