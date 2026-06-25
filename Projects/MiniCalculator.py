print ("WELCOME TO CALCULATOR")


a=int(input("enter 1st digit: "))
z= input("+, -, * , / : ")
b=int(input("enter 2nd digit: "))


if z == "+":
    print(a + b)

elif z == "-":
    print(a - b)

elif z == "*":
    print(a * b)

elif z == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)

else:
    print("Invalid operator")
