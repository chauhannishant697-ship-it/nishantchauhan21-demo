"""
                                PROJECT NAME = QUIZ GAME
"""


print("WELCOME TO THE QUIZ GAME!")

play= input("DO YOU WANT TO PLAY THE GAME.....? YES or NO:  ", ).upper()
if(play!= "YES"):
    print("OKY, PLAY NEXT TIME 😔")
    quit()
elif(play=="YES"):
    name= input("enter your name: ", )
    print(name, "Let`s PLAY the GAME 🥳")
Score= 0
print(".....................................................")

answer1= input("IN BIOLOGY, BASIC UNIT OF LIFE IS CALLED.....? ", ).upper()
if(answer1=="CELL"):
    print("CORRECT ANSWER!....🥳")
    Score += 1
else:
    print("WRONG ANSWER!....😢")


answer2= input("IN BIOLOGY, MITOCHONDRIA IS CALLED.....? ", ).upper()
if(answer2=="POWER HOUSE"):
    print("CORRECT ANSWER!....🥳")
    Score += 1
else:
    print("WRONG ANSWER!....😢")


answer3= input("IN BIOLOGY, LISOSOMES IS CALLED.....? ", ).upper()
if(answer3=="SUCIDAL BAG"):
    print("CORRECT ANSWER!....🥳")
    Score += 1
else:
    print("WRONG ANSWER!....😢")


answer4= input("IN BIOLOGY, NUCLEUS IS CALLED.....? ", ).upper()
if(answer4=="BRAIN OF THE CELL"):
    print("CORRECT ANSWER!....🥳")
    Score += 1
else:
    print("WRONG ANSWER!....😢")


answer5= input("IN BIOLOGY, CELL MEMBRANE IS CALLED.....? ", ).upper()
if(answer5=="WALL OF THE CELL"):
    print("CORRECT ANSWER!....🥳")
    Score += 1
else:
    print("WRONG ANSWER!....😢")


print(name, "YOU COMPLETED YOUR QUIZ.......🥳")
print("YOUR SCORE : ", Score)
print("YOU GOT: ", (Score/5)*100, "%")
