#day1 one of my Python code. 
                             
                                    #First_code

print("Hello World")
print(21)
print(21+21)
print("myself nishant chauhan.","my age 21.")



  
                                   #VARIABLES

"""Rules for variable name 
1= We can use (A to Z), (a to z), (0 to 9), (_). But can not use special characters(@ % $ * etc)
2= Can not start with digit. (Ex- 1variable is incorrect But Variable1 is correct.) 
3= variable name can be any length""" 
                                  
print("VARIABLES")
#Variable : value
name=       "Nishant Chauhan" #type= String
age=        21 #type= Intiger
milk_rate=  55.80 #type= Float

print("my age is",age)
print("my name is",name)
print("Milk rate is",milk_rate,"rupees")




                                   #DATA TYPES

"""There are 5 types of data type:
1= Integer Ex- (-ve) & (+ve) values and (0), -21, +25, -50, etc.
2= String Ex-  'Hello', "Hello", '''Hello''', etc.
3= Float  EX- 21.22, 2.80, 5.66, etc.
4= Bollean = True & False
5= None   Ex- (a= None), so currently here is no value."""  

print(type(name))
print(type(age))
print(type(milk_rate))




                                 #KEYWORDS

"""Keywords are reserved words in python. They have there partiular meanings and they can not use as normal words or variables.....

(and) (as) (assert) (break) (class) (continue) (def) (del) (elif) (else) (except) (finally) (False) (for) (from) (global) (if) (import) (in) (is) (lambda) (nonlocal) (None) (not) (or) (pass) (raise) (return) (True) (try) (with) (while) (yield)
Note: Python is case sensitive language. So must be in mind that what we need to use: capital latters(A to Z) or small latters(a to z)""" 




                                 #CALCULATIONS 

a= 21
b= 4
c= 5
sum= a+b+c
diff= a-b-c

print(sum)
print(diff)




                                  #PUNCTUATORS 
 
"""These are symbols to organize sentences structure in programming. 
# (), {}, [], @, #, etc.
# -=, +=, /=, *=, //=, =, etc"""  





                                  #Rules Of Expression Execution

# RULE 1: String & Numeric values can operate together with * : 
X,Y = 2,4 
txt= "$" 

print(X*txt*Y)
#OUTPUT : $$$$$$$$  

# RULE 2: String & String can operate with + : 
A,B= "@",3
txt= "$"

print((A+txt)*B)
#OUTPUT : @$@$@$

#RULE 3: Numeric values can operate with all arithmetic operators: 
A,B= 5,2
C= 3

print(A+B*C)
#OUTPUT : 11 

#RULE 4 : Arithmetic expression with Integer and float will result in float:
A,B= 2,3.000

print(A*B)
#OUTPUT : 6.0

#RULE 5 : Integer division (//) with float gives round of number in float.
A,B= 12,5
c= A//B 
print(c)
#OUTPUT : 2
 
A,B = 12,-5 
C= A//B 
print(C)
#OUTPUT : -3 

#ONLY DIVISION (/)
A,B=12,5
C= A/B
print(C)
#OUTPUT : 2.4 

#RULE 6 : Reminder is negative when dinominator is negative. 
A,B= 2,-4
C=A%B
print(C)
#OUTPUT : -2 

"""DAY 1 was completed"""