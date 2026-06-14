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







