"""
                                 MINI PROJECT 1 NAME = GUESS THE NUMBER
"""                   

name= input("PLEASE ENTER YOUR NAME:", )

import random
target= random.randint(1,100)

while True:
    guess= (input("GUESS THE CORRECT NUMBER  or  QUIT(Q):", ))
    
    if(guess=="Q"):
        print(name, "LEFT THE GAME WITHOUT COMPLETED 😥")
        break
    guess= int(guess)
    if(guess==target):
        print("SUCCESSFUL....CORRECT GUESS 🥳")
        break

    elif(guess>target):
        print("WRONG....YOUR GUESS IS TOO BIG")

    else:
        print("WRONG....YOUR GUESS IS TOO SMALL")

print("💖...GAME OVER...💖")



"""
                                     MINI PROJECT 2 NAME = RANDOM PASSWORD GENERATOR
"""
import random
import string

n= 12
pas= string.ascii_letters + string.digits + string.punctuation

Password= ""
for i in range(n):
    Password += random.choice(pas)

print("YOUR PASSWORD IS:", Password)

 


"""
                                PROJECT NAME = ROCK, PAPER, SCISSORS (GAME)
"""


#not completely looking well

import random

game= ["ROCK", "PAPER", "SCISSOR"]
i= (random.choice(game))

n= input("Let`s Play- ROCK, PAPER, SCISSOR: " ).upper()


while True:
    if(n==i):
        print("DRAW:🤷‍♂️")
        break
    elif(n!=i):
        if(n== "PAPER" and i== "ROCK"):      #i=ROCK
            print("CORRECT.....YOU WIN 💖")
            break
        elif(n=="SCISSOR" and i== "ROCK"):
            print("INCORRECT.....YOU LOSE 😭")
            break

        elif(n== "SCISSOR" and i== "PAPER"):  #i= PAPER
            print("CORRECT.....YOU WIN 💖")
            break
        elif(n=="ROCK" and i== "PAPER"):
            print("INCORRECT.....YOU LOSE 😭")
            break
        

        if(n== "ROCK" and i== "SCISSOR"):       #i= SCISSOR
            print("CORRECT.....YOU WIN 💖")
            break
        elif(n=="PAPER" and i== "SCISSOR"):
            print("INCORRECT.....YOU LOSE 😭")
            break

print("💖....GAME OVER....💖")








"""
                               PROJECT NAME = CHOOSE YOUR OWN ADVENTURE 
"""

name= input("Type your name: " )
print("Welcome", name, "To The Advanture")

i= input("Chosse your advanture.....for Jungle enter(Jungle) or for Road enter(Road) ").upper()

if(i== "JUNGLE"):
    print("Now, you enter in the jungle")
    n= input("If you want to swim in river enter(SWIM) or If you want to run on ground enter(RUN): ").upper()
    if(n== "SWIM"):
        print(name, "is swiming in river")
        print(name, "enter in the cave")
        print(name, "you collect the gem successfully")
        print("YOU WON THE ADVANTURE")
        print("...............................................")
        print("...GAME OVER...")

    elif(n== "RUN"):
        print(name, "is running on ground")
        print(name, "enter in the cave")
        print(name, "you collect the gem successfully")
        print("YOU WON THE ADVANTURE")
        print("...............................................")
        print("...GAME OVER...")

    

elif(i== "ROAD"):
    print("Now, you are on the Highway")

    z= input("If you want to run on highway enter(HIGHWAY) or If you want to sit in car enter(CAR): ").upper()
    if(z== "HIGHWAY"):
        print(name, "is running on the Highway")
        print(name, "enter in the Building")
        print(name, "you collect the gem successfully")
        print("YOU WON THE ADVANTURE")
        print("...............................................")
        print("...GAME OVER...")

    elif(z== "CAR"):
        print(name, "is sitting in the Car ")
        print(name, "enter in the Building")
        print(name, "you collect the gem successfully")
        print("YOU WON THE ADVANTURE")
        print("...............................................")
        print("...GAME OVER...")


else:
    print("INVALID MOVE......")














