#Class
#constructor - 3 parameters (name,roll,age)
#fun marks(lang,english,maths)
#fun calgrade ()
#distin - 80 abv
#first clas - 60-79
#second class - 40-59
#fail - belw 40


class student:

    def __init__(self,name,rollnum,age):
        self.name = name
        self.rollnum = rollnum
        self.age = age

    def marks(self,lang,english,maths):
        self.lang = lang
        self.english = english
        self.maths = maths
        return int(lang)+int(english)+int(maths)

    def calGrade(self):
        marks = self.marks(self.lang,self.english,self.maths)
        print("Total Marks--->",marks)

        #dist
        if (marks//3) >=80:
            return "First Class with Distinction"
        #First class
        elif (marks//3) >=60:
            return "First Class"
        #Second Class
        elif (marks//3) >=40:
            return  "Second Class"
        #Fail
        else:
            return "Fail"

print('************************************')
student1 = student("Dhoni",7,20)
student1.marks(75,45,80)
print(student1.name,"Marks Chart")
print(student1.calGrade())


print('************************************')
student2 = student("Virat",18,18)
student2.marks("75","80","99")
print(student2.name,"Marks Chart")
print(student2.calGrade())

print('************************************')
student3 = student("Rohit",45,20)
student3.marks(15,45,8)
print(student3.name,"Marks Chart")
print(student3.calGrade())


print('************************************')
student4 = student("Yuvi",12,20)
student4.marks(55,45,57)
print(student4.name,"Marks Chart")
print(student4.calGrade())


