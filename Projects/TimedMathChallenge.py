import random
import time

MIN_VAL = 3
MAX_VAL = 20
OPERATORS = ["+", "-", "*"]
TOTAL_Q = 10

def math_problem():
    num1= random.randint(MIN_VAL, MAX_VAL)
    num2= random.randint(MIN_VAL, MAX_VAL)
    operator= random.choice(OPERATORS)

    expression = str(num1) + " " + operator + " " + str(num2)
    answer = eval(expression)
    return expression, answer

wrong = 0
start_time = time.time()
for question in range(TOTAL_Q):

    expression, answer = math_problem() 
    while True:
        solve= input(f"Problem #{question+1}: {expression} = ") 
        if solve== str(answer): 
            break

        else:
            wrong += 1
            print("Wrong! Try again.")

end_time = time.time()
total_time = round(end_time - start_time, 3)

print("\n🎉 Game Over!")
print(f"Total Time: {total_time} seconds")
print(f"Wrong Attempts: {wrong}")

