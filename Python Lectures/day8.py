"""
This is DAY 8 of Learning PYTHON
"""

                                       #OOPS(part1)= Object Oriented Programming System
"""
OOPS used to map real world scenarios, we started using objects in code. 
"""

                                     # CLASS & OBJECT in PYTHON
"""
Class is a blueprint of object, it is a template for creating objects.
Object is an instance of class, it is a real world entity.

class SYNTAX:
class class_name:
pass          (example: name= "nishant")

Object SYNTAX:
object_name= class_name()   

""" 
#basic class & object code:
class Student:
    name= "ANU"
    age= 21
    f_name= "MR. CHAMAN"
    kaksha= "12th"

s1= Student()
print(s1.name)
print(s1.age)
print(s1.f_name)
print(s1.kaksha)

print("NEXT TOPIC")
                                        #__init__ Function in PYTHON
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

#SYNTAX: 
class Car:
    def __init__(self, xyz):   #self likhna important hota ha
        self.name= any_name
"""

class Team:
    def __init__(self, color):
        self.name= "RCB"
        self.color= color

t1= Team("RED")
print(t1.name)
print(t1.color)


                                            #STATIC Method
"""
Methods that dont use the self perameter (work at class level)
SYNTAX:
class Car:

    @staticmethod
    def hello():
        print("Hello")
"""                                            

                                             #Abstraction
"""
Hiding the un important details of a class and only showing the important features to the user.
"""

                                            #Encapsulation
"""
Wrapping data and function into a single unit(object).
"""

# small program of bank account made by be after 100 time errors 😭😭😭:
class Account:
    
    def __init__(self, bal, acc):
        self.bal= bal
        self.acc= acc

    def credit(self, amount):
        self.bal += amount
        print("Rs.", amount , "HAS BEEN CREDITED")
        print(self.bal)

    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "HAS BEEN DEBITED")  
        print(self.bal)

acc1= Account(100, 21)
print("TOTAL AMOUNT:" , acc1.bal)
print("ACCOUNT NO.:", acc1.acc)

acc1.debit(15) #spend on chips
acc1.debit(50) #spend on phone cover
acc1.credit(500) #given by Nani

print("REMANING BALANCE:" , acc1.bal)


"""
END OF CLASS OOPS PART1
"""

