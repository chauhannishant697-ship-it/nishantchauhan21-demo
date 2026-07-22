M_pwd= input("Enter Your MASTER PASSWORD: ").upper()

if M_pwd!= "A1B2C3" :
    print("WRONG PASSWORD")
    quit()

else: 
    print("CORRECT PASSWORD")

def view():
    account_name= input("Enter Your Account Name: ")
    found= False
    with open("password_file.txt", "r") as f:

        for line in f:
            account, password = line.strip().split(" : ")

            if account.lower() == account_name.lower():
                found= True
                print(f"Account: {account} \nPassword: {password}")
                break

        if not found: 
            print("Account Not Found") 
                
def add():
    name= input("Account Name: ")
    pwd= input("Your Password: ")

    with open("password_file.txt", "a") as f:
        f.write(f"{name} : {pwd} \n")

while True:
    mode= input("You Want To Add a New Password or View old Password(add/view), If you want to quit enter (Q) ").upper()

    if(mode== "Q"):
        break

    elif(mode== "ADD"):
        add()

    elif(mode== "VIEW"):
        view()

    else:
        print("INVALID KEYWORD")
        continue
    

