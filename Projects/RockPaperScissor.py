
                                #PROJECT NAME = ROCK, PAPER, SCISSORS (GAME)

import random

def win():
    print(f"Your Choice: {user_choice} and Opponent Choice: {rand_choice}")
    print(f"You WIN")
    print("Your Total Score: ", score)

def lose():
    print(f"Your Choice: {user_choice} and Opponent Choice: {rand_choice}")
    print(f"You LOSE")

def draw():
    print(f"Your Choice: {user_choice} and Opponent Choice: {rand_choice}")
    print(f"DRAW")  
    print("Your Total Score: ", score)
    
name= input("ENTER YOUR NAME: ")
game= ("ROCK", "PAPER", "SCISSOR")
score= 0

while True:
    permission= input("For Play Press (P) and For Quit Press (Q): ").upper()
    if permission== "P":
        print("Let`s Play")

        user_choice= input("Choose ROCK, PAPER, SCISSOR: ").upper()
        rand_choice= random.choice(game)

        if user_choice== rand_choice:
            draw()

        else:
            if user_choice== "ROCK" and rand_choice== "SCISSOR":
                score+= 5
                win()

            elif user_choice== "PAPER" and rand_choice== "ROCK":
                score+= 5
                win()

            elif user_choice== "SCISSOR" and rand_choice== "PAPER":
                score+= 5
                win()

            elif user_choice!= "ROCK" and user_choice!= "PAPER" and user_choice!= "SCISSOR" :
                print("Invalid Request!")

            else:
                score-= 3
                lose()
                if score < 0:
                    score=0
                    print(f"YOUR SCORE: {score}")

                else:
                    print(f"Your Total Score: {score}")

    elif permission== "Q":
        print("THANKS FOR PLAYING")
        print("Your Total Score: ", score)
        break

    else:
        print("INVALID REQUEST!")


