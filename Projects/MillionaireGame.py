print("Who wants to be a Millionaire")

def Millionaire():
    correct_answers= 0
    total_prize= 0
    questions= [
        ["Question 1: Capital of India ?",            
            "A. Mumbai",
            "B. Delhi",
            "C. Jaipur",
            "D. Chennai",

            "B"
        ],

        ["Question 2: 2 + 5 = ?",          
            "A. 7",
            "B. 5",
            "C. 9",
            "D. 8",

            "A"
        ],            

        ["Question 3: Power House of the cell ?",
            "A. Lisosomes",
            "B. Mitochondria",
            "C. Nucles",
            "D. Plasma Membrane",  

            "B"        
        ],

        ["Question 4: 3 x 7 = ?",
            "A. 29",
            "B. 25",
            "C. 21",
            "D. 36",

            "C"
        ],

        ["Question 5: Value of Pie = ?",
            "A. 23/7",
            "B. 4.244",
            "C. 1.322",
            "D. 3.142",

            "D"
        ],

        ]

    prize= [ 5000, 10000, 25000, 32000, 50000]

    for q in questions:
        print(q[0])
        print(f"a. {q[1]}")
        print(f"b. {q[2]}")
        print(f"c. {q[3]}")
        print(f"d. {q[4]}")

        answer= input("CHOOSE CORRECT OPTION: ").upper()

        if answer == q[5]:
            print('CORRECT ANSWER......')
            
            for p in prize:
                total_prize += p
                print(f"YOU WON : {total_prize}")

        else:
            print("WRONG ANSWER......")
            break

    print("YOUR TOTAL WINNING AMOUNT IS: ", total_prize )

Millionaire()














"""
print("Who wants to be a Millionaire")

def Millionaire():
    correct_answers= 0
    total_prize= 0
    questions= [
        ["Question 1: Capital of India ?",            
            "A. Mumbai",
            "B. Delhi",
            "C. Jaipur",
            "D. Chennai",
        ],

        ["Question 2: 2 + 5 = ?",          
            "A. 7",
            "B. 5",
            "C. 9",
            "D. 8",
        ],            

        ["Question 3: Power House of the cell ?",
            "A. Lisosomes",
            "B. Mitochondria",
            "C. Nucles",
            "D. Plasma Membrane",          
        ],

        ["Question 4: 3 x 7 = ?",
            "A. 29",
            "B. 25",
            "C. 21",
            "D. 36",
        ],

        ["Question 5: Value of Pie = ?",
            "A. 23/7",
            "B. 4.244",
            "C. 1.322",
            "D. 3.142",
        ],

        ]

    answers= [ "B", "A", "B", "C", "D"]

    for i in range(len(questions)):
        user = input(questions[i])

    if user == answers[i]:
        print("Correct")
    else:
        print("Wrong")


Millionaire()
"""
























