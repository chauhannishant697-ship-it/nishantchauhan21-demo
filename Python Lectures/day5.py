"""
DAY 5 OF LEARNING PYTHON
"""

                                    #LOOPs IN PYTHON
"""
LOOPS are used to repeat instructions.
"""

#WHILE LOOP:
"""
SYNTAX= while (condition):
              #some work
"""

#To write "HELLO" infinite times:
"""
i=1
while True:
    print("HELLO", i)
    i += 1

NOTE: NEVER CREATE A INFINITE LOOPS IN REAL LIFE CODING, IT CRASH OUR SYSTEM.
"""

#To print "Hello" 5 times: 
x= 1
while x <= 5:
    print("Hello")
    x +=1

print(x)

#To print counting 1 to 5 :
i=1
while i <= 5:
    print(i)
    i +=1

#To print counting 5 to 1 :
i=5
while i >= 1:
    print(i)
    i -= 1
print("end loop")

#To print LIST in terms of loop:

plyr = ["VIRAT", "ROHIT", "DHONI", "RAJAT", "TIM DAVID"]

i=0
while i < len(plyr):
    print(plyr[i])

    i = ( i + 1)

                                                   #BREAK & CONTINUE
"""
BREAK: Used to end the loop when wanted value Found.
CONTINUE: To SKIP 
"""

                                                 #FOR in loop
#Q1.
movies= ["DDLJ", "I", "PK", 96, ]

for FILM in movies:
    print(FILM)            #Ye FILM me ek ek krke movies ki values ko print kraga. 

#Q2. 
nums= [1,4,7,2,8,000]

for x in nums:
    print(x)

#Q3. 
str= "@MYSELF21"

for i in str:
    print(i) 

#FOR is not completely clear 

                                       #RANGE()
"""
RANGE function returns a sequence of numbers, start from 0 by default, and increments by 1 (by default), and stop before a specific number.
SYNTAX= for x in range(start, stop, step):                                
"""

#To print ODD numbers till 100:

for i in range(1,100,2):
    print(i)
    
#To print any number table :
X= int(input("enter by user:", ))
for mul in range(1,11,1):
    print(mul * X)


                                       #PASS Statement
"""
pass is a null statement that do nothing but it hold place for future code.
"""



                