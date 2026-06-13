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









