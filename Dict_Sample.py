#dict ordered, mutable
#key-value pair
#duplicates for value but nt for key

thisdict = {
    "Fruit" : "Apple",
    "Color" : "Red",
    "Region" : "Kashmir",
     2020:"Current year",
    "covid": 2020,
    "Color": "Green"

}
print(thisdict)
print(thisdict[2020])
print(thisdict.get(2020))
print(thisdict["Color"])
print("-----------------------")
#to get keys
for t in thisdict:
    print(t)
print("-----------------------")

for t in thisdict.keys():
    print(t)
print("-----------------------")

#to get the values
for t in thisdict:
    #print(thisdict[t])
    print(thisdict.get(t))
print("-----------------------")
for t in thisdict.values():
    print(t)
print("-----------------------")

#to get the item

def getKey(val):
    for key,value in thisdict.items():
        if val == value:
            return key

    return "Key doesnt exist"

thisdict = {
    "Fruit" : "Apple",
    "Color" : "Red",
    "Region" : "Kashmir",
     2020:"Current year",
    "covid": 2020,
    "Color": "Green"

}
print(getKey("Kashmir"))


for key,value in thisdict.items():
    print(key)
    print(value)
print("-----------------------")

#######################
newdict = thisdict.copy()
print(newdict)

newdict.clear()
print(newdict)

#set() - empty set and {} =  empty dict

#pop - we need to specify key as input, it will remove it
thisdict.pop("Color")
print(thisdict)


#popitem - it willremove lastone
#thisdict.popitem()
print(thisdict)

#update
thisdict.update({"covid":"End is here"})
print(thisdict)

#setdefault
thisdict.setdefault("covid","end is here in 2020")
#print(x)
print(thisdict)

thisdict.setdefault("covid 19","end is here in 2020")
print(thisdict)