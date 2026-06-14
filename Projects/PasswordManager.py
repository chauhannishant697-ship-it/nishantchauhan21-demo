M_pwd= input("Enter Your MASTER PASSWORD ", )

def view():
    with open("nishantchauhan21-demo\Python Lectures\DemoFile.txt", "r") as f:
        for lines in f.readlines():
            print(lines)


def add():
    name= input("Account Name: ", )
    pwd= input("Your Password: ", )

    with open("nishantchauhan21-demo\Python Lectures\DemoFile.txt", "a") as f:
        f.write(name+ ": " + pwd+ "\n")

while True:
    mode= input("You Want To Add a New Passward or View old Password(add/view), If you want to quit enter (Q) ").upper()

    if(mode== "Q"):
        break

    if(mode== "ADD"):
        add()

    elif(mode== "VIEW"):
        view()

    else:
        print("INVALID KEYWORD")
        continue
    




