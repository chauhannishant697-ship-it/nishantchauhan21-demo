"""
This is a day 6 of learning Python.
"""

                                      #FUNCTION in PYTHON
"""
function is a block of code which is used to perform a specific task.
SYNTAX of function is: def func_name():
    #some work
"""

#To divide two numbers multiple time, firstly we write this type of code, then divide different different numbers many times:  
def div_num(a,b):
    div_num= a / b 
    print(div_num)
    return div_num

#this is called calling the function.

sum= div_num(99,33) #function call

taxt= div_num(20, 5) #function call 

#Now after many lines of code we can use same function by function call.

# To multiply two numbers many times by single code:

def nikki(a,b):
    channu = a * b
    print(channu)
    return channu

nikki(4,5)

#For average of three num:

def avg_num(a,b,c):
    i= (a+b+c)/3
    return i 


x= avg_num(4,6,2)
print(x)

y= avg_num(3,6,30)
print(y)

#To print length of list: 

def i(s):
    print(len(s))

movie= [96,"I", "DDLJ"]
bag= ["pencil","rubber", "sharpner", "scale", "books"]

i(movie)
i(bag)

house= ["bedroom", "kitchen", "bathroom", "guestroom"]

i(house)




                                  # Type of FUNCTIONS in PYTHON
"""
There are two types of functions:

Built-in Functions:                                  
                                                   
print()                                              
len()
type()
range()
etc.........

User defined functions:  They are made by us......
"""

#print function:

print("anu \naru") # to print in new line we use \n.

print("anu \t aru") # to print in tab space we use \t.

print("anu","aru","nikki", sep=" $$ ") # to separate the words by * we use sep=" $$ ".

#len function:
i= "anu"
print(len(i)) # to find the length of string we use len() function. 

#type function:
a= 5.00
print(type(a)) # to find the type of variable we use type() function.

#range function:
for i in range(1,10):
    print(i) # to print the numbers from 1 to 9 we use range() function.


#default argument in function:
def default_arg(a,b=5):
    c= a + b
    print(c)
    return c

default_arg(45) # here we only pass one argument because the second argument is default argument.


                                    #RECURSION in PYTHON
"""
Recursion is a process of calling a function inside itself. It is used to solve problems which can be broken down into smaller sub-problems.
"""
def mul(a):
    if(a==0):
        return 5
    print(a)
    mul(a-1) # recursive call   

# print numbers from 1 to 5 using recursion
"""
# FUNCTION CREATE KIYA
def count(n):

    # STOPPING CONDITION
    # AGAR n KI VALUE 6 HO JAYE TO FUNCTION STOP
    if(n == 6):
        return

    # CURRENT VALUE PRINT KAR RAHA HAI
    print(n)

    # RECURSION
    # FUNCTION KHUD KO DOBARA CALL KAR RAHA HAI
    # n+1 KA MATLAB NEXT NUMBER
    count(n + 1)

# FUNCTION START KIYA
# YAHA SE RECURSION CHALU HOGA
count(1)
"""
#To print numbers from 10 to 1:
def write(n):
    if(n==0):
        return
    
    print(n)

    write(n-1)
write(10)

#To print table of 5:
n=5
def mul(i):
    if(i==11):
        return
    
    print(n * i)
    mul(i + 1)

mul(1)

#CHAPTER COMPLETED


""" 
END OF DAY 6 
"""