#!usr/bin/python
#Filename:inherit.py

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print"Initiatlizing %s" %self.name
    def tell(self):
        print"%s's age is %s" %(self.name,self.age)

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print"Teacher's name is %s" %self.name
        print"Teacher's age is %s" %self.age
    def tell(self):
        SchoolMember.tell(self)
        print"Teacher's salary is %s" %self.salary

class Student(SchoolMember):
    def __init__(self,name,age,mark):
        SchoolMember.__init__(self,name,age)
        self.mark=mark
        print"Student's name is %s" %self.name
        print"Student's age is %s" %self.age
    def tell(self):
        SchoolMember.tell(self)
        print"Student's mark is %s" %self.mark

a=Teacher("leo","24","10000")
b=Student("Eric","12","80")
Members=[a,b]
for member in Members:
    member.tell()
