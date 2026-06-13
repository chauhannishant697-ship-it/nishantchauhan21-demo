"""
This is 9th day of learning python 
"""

                                     # OOPS in Python

"""
del keyword used to delete object properties or object it self.
SYNTAX: 
class Car:
    def __init__(self, name):
        self.name = name
                                
c1= Car("ROLLS ROYALS")
print(c1.name)

del c1.name     # This is acctual syntax to delete object or object property.
print(c1.name)                               
"""

                                   #Private(like) attributes & method
"""
class Acc:
    def __init__(self, acc_no, acc_pass):
        self.acc_no= acc_no
        self.acc_pass= acc_pass      

a1= Acc("12345", "a1b2c3")
print(a1.acc_no)
print(a1.acc_pass)    #use, __acc_pass, to private your password.

# Esa krne se dono output me show ho jayangi but password to private & sensitive hota ha to usko publically nhi show kr sakte to es liye 
hum likhange : __acc_pass............ ye krne se password show nhi hoga and error show hoga.
"""

                                    #Inheritance
"""
When one class(child class) derives the properties & methods of another class(parent class)
SYNTAX:
class Car:
    ........
    ........

.................
.................

class ToyotaCar(Car):
    ........


                               #Types of Inheritance
Single Inheritance
Multi-level Inheritance
Multiple Inheritance                               
"""

                                    #Super Method
"""
Super() method is used to access methods of the parent class.
SYNTAX:
super().__init__()
"""

                                    #Class Method
"""
A class method is bound to the class & receives the class as an implicit first argument. 
NOTE: static method can`t access of modify class state & generally for utility.

SYNTAX:
class Student:
    @classmethod
    def college(cls):
        pass
"""

                                #Property method
"""
We use @property derector on any method in the class to use the method as a property.
"""



                                 # Polymorphism: Operator Overloading
"""
When the same operator is allowed to have different meaning according to the context.
"""

# __add__  dunder function
class Num:
    def __init__(self, real, img):
        self.real= real
        self.img= img

    def showNum(self):
        print(self.real, "i+", self.img,"j")

    #__add__  dunder function used
    def __add__(self, num2):           
        newReal= self.real + num2.real
        newImg= self.img + num2.img
        return Num(newReal,newImg)

num1= Num(3,7)
num1.showNum()

num2= Num(2,5)
num2.showNum()

num3= num1 + num2
num3.showNum()

# To write this simple code i rewatch lecture multiple time and got error 10+ times, then i write this means my OOPS topic is very week.

"""
PRACTICE SOME QUESTIONS:
"""

#QUES1. 
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
# small program of bank account made by be after 100 time errors , 100 time see lecture 100 time search on chat gpt 😭😭😭.


#QUES 2. 
#Find area & perimeter of circle by using OOPS:
class Circle:
    def __init__(self, radius):
        self.radius= radius

    def area(self):
        area= (22/7)*self.radius*self.radius
        print("AREA OF CIRCLE:", area)
        return Circle

    def per(self):
        per=  2*(22/7)*self.radius
        print("PERIMETER OF CIRCLE:", per)
        return Circle

c1 = Circle(5)
c1.area()
c1.per()

c2 = Circle(21)
c2.area()
c2.per()         
# I solved this without see in lecture & got 5 times Error then complete but i did not write it acctually like lecture😕

 
#QUES3. 
class Employee:
    
    def __init__(self,role,dept,salary):
        self.role= role
        self.dept= dept
        self.salary= salary

    def showDetail(self):
        print("role:", self.role)
        print("dept:", self.dept)
        print("salary:", self.salary)

E1 = Employee("HR","AI", "21,000")
E1.showDetail()

class Engineer(Employee):
   
    def __init__(self,name,age,role,dept,salary):

        super().__init__(role,dept,salary)

        self.name= name
        self.age= age

    def showOther(self):
        print("NAME:", self.name)
        print("AGE:", self.age)
        print("ROLE:", self.role)
        print("DEPARTMENT:", self.dept)
        print("SALARY:", self.salary)

En1= Engineer("NIKKI", "21", "MANAGER", "AI/ML", "80,000")
En1.showOther()
#done without watching lecture BUT 15+ times error found then help with gpt for syntax then done.


"""
DAY(9) COMPLETED 
"""
#THE TOPIC : OOPS IS ALSO MY WEEK AREA.   








