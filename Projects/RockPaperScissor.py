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
