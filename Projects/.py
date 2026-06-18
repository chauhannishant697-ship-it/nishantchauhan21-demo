import random
import time

MIN_VAL = 3
MAX_VAL = 20
OPERATORS = ["+", "-", "*"]
TOTAL_Q = 10

def math_problem():
    i = random.randint(MIN_VAL, MAX_VAL)
    j = random.randint(MIN_VAL, MAX_VAL)
    op = random.choice(OPERATORS)

    expression = str(i) + " " + op + " " + str(j)
    answer = eval(expression)

    return expression, answer


wrong = 0

start_time = time.time()

for z in range(TOTAL_Q):

    expression, answer = math_problem()

    while True:

        guess = input(f"Problem #{z+1}: {expression} = ")

        if guess == str(answer):
            break

        wrong += 1
        print("Wrong! Try again.")

end_time = time.time()

total_time = round(end_time - start_time, 2)

print("\n🎉 Game Over!")
print(f"Total Time: {total_time} seconds")
print(f"Wrong Attempts: {wrong}")