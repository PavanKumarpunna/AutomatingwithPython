## For loop

for i in range (10):
    print(i)

# range will take 3 parameters- 2 are optional, 1 is mandatory
# range will accept only integer parameter
# by default start ->0 an step ->1
for i in range(10): #if its 1 parameter, then it will treat as stop
    print(i)

for i in range(10,20): #if its 2 parameters, then it will start as first parameter and stop as second
    print(i)

for i in range(0,200,10): #3 parameters, start,stop and step, for using step: start and stop are mandatory
    print(i)

str = "India"
for s in str:
    print(s)

for c in range(len(str)):
    print(str[c])

for s in str:
    #print(s)
    if s == 'd':
        print("d is pres")
        break

for s in str:
    #print(s)
    if s == 'd':
        print("d is pres")
        continue
        print('India')
