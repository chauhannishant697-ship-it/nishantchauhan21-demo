"""
                                PROJECT NAME = PIG GAME
"""

import random
name= input("ENTER YOUR NAME: ").upper()
print("WELCOME", name, "TO THE GAME")

score= 0
while True:
    i= input("You Have a Dice, If You Want To ROLL press (R) or If You Want To Hold press (H): ").upper()

    if(i== "H"):
        break

    elif(i== "R"):
        n= random.choice([1,2,3,4,5,6])
        print(n)

        if(n==1):
            score= 0
            print("YOU LOOSE YOUR ALL POINTS & AND YOUR SCORE IS: ", score)
            break
            
        elif(n!=1):
            score= score + n
            print("YOUR CURRENT SCORE:", score)

    else:
        print("INVALID MOVE......PLEASE CHOOSE (R) or (H)")




