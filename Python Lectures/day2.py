                                       #COMMENTS IN PYTHON 

"""THERE ARE TWO TYPES OF COMMENTS 1= BY # & 2= BY triple code"""


                                           #INPUT IN PYTHON
"""It means taking value from user: 
1. Srting Input 
name= input("my name is:", ) 

2. Integer Input 
age= int(input("my age is:", ))

3. Float Input 
Milk_price= float(input("milk price is:", ))"""


                                       #Conditional Statements
"""
if-elif-else(SYNTAX)

if(condition):
    Statement 1

elif(condition):
    Statement 2

else:
    Statement xyz
"""    

light= input("Enter by user:", )

if(light == "Green"):
    print("GO")

elif(light == "Yellow"):
    print("LOOK")

elif(light == "Red"):
    print("STOP")

else:
    print("LIGHT IS BROKEN")

    

"""
NESTING = EK STATEMENT KE ANDER DUSRI STATEMENT KO LIKHNA
"""



"""                                       SINGLE LINE CONDITIONS                                                  
1. Variable= "val1" if (condition) else "val2" 
"""

RCB= input("enter by user:", )

X = "TROPHY" if RCB=="win" else "BETER LUCK NEXT TIME"
print(X) 

"""
2. (Statement1) if (condition) esle (statement2)
"""
c= input()

print("crazy") if c=="Z" else print("fuck")





                                             #TYPE OF OPERATORS 
"""
OPERATORS are the symbols that perform certain operations.
"""
# 1. Aritmetic Operators  : (+, -, *, /, %, **)

a= 2
b= 3

sum= a+b 
sub= a-b 
mul= a*b
div= a/b
rem= a % b
power= a**b 

print(sum)
print(sub)
print(mul)
print(div)
print(rem)
print(power)

# 2. Relation Operators   : (==, !=, >, <, >=, <=)
"""
 (==) means is equal to  & (!=) means is not equal to
""" 
a= 21 
b= 121

print(a==b) #False
print(a!=b) #True 
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True

# 3. Assignment Operators : (=, =+, -=, *=, /=, %=, **=)
"""
THIS TOPIC IS NOT COMPLETELY CLEAR, I HAVE SOME CONFUSION.
"""

# 4. Logical Operators    : (not, and, or)

print( not True ) #OUTPUT : False
print( not False) #OUTPUT : True

"""
THIS TOPIC IS ALSO NOT COMPLETELY CLEAR, I HAVE SOME CONFUSION.
"""

                                               #STRING

"""
WE CAN WRITE STRING IN THREE WAYS :
('HELLO')
("HELLO")
('''HELLO''')

WE CAN USE (\n) FOR NEXT LINE & (\t) FOR TAB SPACE:
"""

STR1= "MYSELF NISHANT CHAUHAN.\n MY AGE IS 21."
print(STR1)

STR2= "MY FAV NO. IS: \t 21"
print(STR2)

"""
BASIS OPERATIONS IN STRING :

1. CONCATENATION & LENGTH OF STRING: SYNTAX= (len(str))
"""

str1= "HELLO " 
str2= " WORLD"

X = (str1+ str2)
print(X)              #OUTPUT : HELLO  WORLD

print(len(str1))      #OUTPUT : 6

"""
2. INDEXING 
SYNTAX= str[ANY NO.]
and INDEXING start with [0] & also count spacings.
"""
str= "MYSELF 21"

print(str[5])         #OUTPUT : F 

"""
3. SLICING 
Used for Accessing parts of a String. It start with O to end length of string.
SYNTAX = str[starting index : ending index]
"""

str= "MY NAME IS NISHANT CHAUHAN 21"

print(str[3 : 21])    #OUTPUT : NAME IS NISHANT CH

"""
There is a negative index slicing also present in python language. It start with -1 to starting of string.
SYNTAX: for ex-  A  P  P  L  E
                -5 -4 -3 -2 -1
str[-4: -2]           #OUTPUT : PP
"""

                                      #STRING FUNCTION 
str= "MY NAME IS NISHANT CHAUHAN"

print(str.endswith("HAN")) 
#If yes it print True, If not it print False. 

print(str.capitalize())
#It capital first letter of your string. 

print(str.replace("IS", ":"))
#It replace "IS" with ":"

print(str.find("A"))
#It print no. where this letter present firstly, Here : 4

print(str.count("N"))
#It print that this how many times this letter present in your string, Here : 4


"""
END OF DAY 2
"""








