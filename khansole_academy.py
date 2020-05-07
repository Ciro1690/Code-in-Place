"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

LOW_NUM = 10
HIGH_NUM = 99
WINNING = 3
def main():
    """
    Pre: takes in constants of LOW_NUM at 10, HIGH_NUM at 99 and WINNING at 3.
    Post: generates two random numbers between the values of LOW_NUM and HIGH_NUM and asks user for the sum of the two values.
    If user answers correctly, the count goes up by 1 until it reaches WINNING. If incorrect, count goes back to 0.
    """
    count = 0
    while count != WINNING:
        num_1 = random.randint(LOW_NUM, HIGH_NUM)
        num_2 = random.randint(LOW_NUM, HIGH_NUM)
        correct = num_1 + num_2
        num_3 = int(input("What is " + str(num_1) + " + " + str(num_2) + "? "))
        if num_3 == correct:
            count += 1
            print("Correct! You've gotten " + str(count) + " correct in a row.")
        else:
            print("Incorrect. The correct answer is " + str(correct) + "." )
            count = 0
    print("Congratulations! You've mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
