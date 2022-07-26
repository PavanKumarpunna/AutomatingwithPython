#while - Stop point

i = 0
while (i<=10):
    print(i)
    i=i+1

for i in range(0,11,1):
    print(i)

#Reversing a number
number = 15975
#Output = 57951
reverse = 0
while (number>0):
    remainder = number%10 # remainder  - 5
    reverse = (reverse * 10) + remainder #- 0+5
    number = number // 10 # Quotient - 1597
print(reverse)

strnum = str(15975)
print(strnum)
print(type(strnum))
print(strnum[::-1])

