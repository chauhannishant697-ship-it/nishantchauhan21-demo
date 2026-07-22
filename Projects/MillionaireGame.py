print("Who wants to be a Millionaire")

def Millionaire():

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
    i=0

    for q in questions:
        print(q[0])
        print(f"a. {q[1]}")
        print(f"b. {q[2]}")
        print(f"c. {q[3]}")
        print(f"d. {q[4]}")

        answer= input("CHOOSE CORRECT OPTION: ").upper()
        
        if answer == q[5]:
            print('CORRECT ANSWER......')
            print("YOU WON: ", prize[i])
            i += 1

        else:
            print("WRONG ANSWER......")
            break
        
Millionaire()
