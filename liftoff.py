"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    Prints numbers 10 to 1 in descending order, followed by LiftofF!
    """
    num = 10
    for i in range (10):
        print (num)
        num-=1
    print ("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
