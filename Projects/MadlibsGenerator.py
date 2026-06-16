"""
                                   Project Name = Madlibs Generator                   
"""

def words():
    name= input("PERSON : ").upper()
    animal= input("ANIMAL: ").upper()
    personality= input("PERSONALITY: ").upper()
    print(f"One day {name} was running in the jungle.Suddenly a giant {animal} appeared. Instead of running away, {name} adopted the {animal}.Now both of them are extremely {personality}.")
   
while True:
    user_choice= input("FOR GENARATING STORY press (W), or FOR QUIT press (Q): ").upper()

    if(user_choice== "W"):
        words()
        break

    elif(user_choice== "Q"):
        print("OKY.....GENERATE NEXT TIME")
        break
    else:
        print("INVALID INPUT, PLEASE ENTER (W) For STORY or (Q) For Quit")















