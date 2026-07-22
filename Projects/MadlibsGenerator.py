"""
                                   Project Name = Madlibs Generator                   
"""
def generate_story():
    name= input("PERSON : ").upper()
    animal= input("ANIMAL: ").upper()
    personality= input("PERSONALITY: ").upper()
    print(f"One day {name} was walking through a jungle. Suddenly, a giant {animal} appeared. Surprisingly, instead of running away, {name} befriended the {animal}. Soon they became the {personality} duo in the forest.")
   
while True:
    user_choice= input("FOR GENARATING STORY press (W), or FOR QUIT press (Q): ").upper()

    if(user_choice== "W"):
        generate_story()

    elif(user_choice== "Q"):
        print("OKY.....GENERATE NEXT TIME")
        break

    else:
        print("INVALID INPUT, PLEASE ENTER (W) For STORY or (Q) For Quit")



