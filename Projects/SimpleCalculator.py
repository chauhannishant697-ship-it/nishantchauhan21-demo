print ("WELCOME TO CALCULATOR")

def calculator(num1,num2,operator):

    if operator== "+":
        print(f"{num1} + {num2} : {num1+num2} ")

    elif operator== "-":
        print(f"{num1} - {num2} : {num1-num2} ")

    elif operator== "*" :
        print(f"{num1} * {num2} : {num1*num2} ")

    elif operator== "/":
            
        if num2 == 0:
            print("ZERO DIVISION ERROR")
        else:
            print(f"{num1} / {num2} : {num1/num2} ")

    else:
        print("ENTER A VALID OPERATOR")

while True:
    calculator(int(input("Enter First Number: ")),int(input("Enter Second Number: ")),input("Enter Operation [+, -, *, /]: "))
    choice = input("For Quit Press (Q) for continue press ENTER: ").upper()

    if choice== "Q":
        break










