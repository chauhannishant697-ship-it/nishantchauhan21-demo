"""
                                           PROJECT NAME = TIMED MATH CHALLENGE 
"""

import random
import time

def add():
    a= random.randint(1,99)
    b= random.randint(1,99)
    c= a+b

    i= int(input(f"{a} + {b}: "))
    score = 0
    if(i==c):
        print("CORRECT....")
        score += 1
        print("YOUR SCORE: ",score)

    elif(i!=c):
        print("INCORRECT... RIGHT ANSWER IS: ", c)
        score= score
        print('YOUR SCORE: ',score)
        
def sub():
    a= random.randint(1,99)
    b= random.randint(1,99)
    c= a-b

    i= int(input(f"{a} - {b}: "))
    score = 0
    if(i==c):
        print("CORRECT....")
        score += 1
        print("YOUR SCORE: ",score)

    elif(i!=c):
        print("INCORRECT... RIGHT ANSWER IS: ", c)
        score= score
        print('YOUR SCORE: ',score)

choice=input("DO YOU WANT TO PLAY A GAME? (YES/NO): ").upper()

count= 0
start_time= time.perf_counter()

while count < 5:
    if choice== "YES":
        print("LETS PLAY")

    elif choice== "NO":
        print("PLAY NEXT TIME.......")
        break

    else:
        print("INVALID MOVE! PLEASE ENTER YES or NO")
        break

    add()
    count += 1
    
while count < 5:
    if choice== "YES":
        print("LETS PLAY")

    elif choice== "NO":
        print("PLAY NEXT TIME.......")
        break

    else:
        print("INVALID MOVE! PLEASE ENTER YES or NO")
        break


    sub()
    count +=1
       
end_time= time.perf_counter()
Total_Time_Taken= end_time - start_time
print(Total_Time_Taken,"Seconds")

print("BEST OF LUCK FOR FUTURE")









