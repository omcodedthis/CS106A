"""
File: khansole_academy.py
-------------------------
Your program should be able to generate simple addition problems that
involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be
asked for an answer to each problem. Your program should determine if the answer was
correct or not, and give the user an appropriate message to let them know. Your program
should keep giving the user problems until the user has gotten 3 problems correct in a row.
"""

import random


def main():
    CORRECT_IN_A_ROW = 0

    while CORRECT_IN_A_ROW != 3:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        correct_answer = num1 + num2
        user_answer = int(input("Enter your answer: "))
# This section of the body generates a simple addition problem by creating two random integers. The correct answer is
# then assigned to a variable "correct_answer" & and the user is asked for an answer which is stored in "user_answer".



        if user_answer == correct_answer:
           CORRECT_IN_A_ROW += 1
            if CORRECT_IN_A_ROW == 3:
                print("Correct! You have gotten 3 in a row.")
                print("Congratulations! You have mastered addition.")
            # This section runs when the user has gotten a streak of 3 correct problems in a row and the program ends.

            print("Correct! You have gotten " + str(CORRECT_IN_A_ROW) +" correct in a row.")
            # This section runs when the score streak is less than 3, and is then repeated by
            # generating another problem.


        else:
            CORRECT_IN_A_ROW = 0
            print("Incorrect. The expected answer is " + str(correct_answer) + ".")
        # This section runs when the user's answer is incorrect, and the score streak is then reverted back to 0.
        # The body is then repeated, generating a new problem.







# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
