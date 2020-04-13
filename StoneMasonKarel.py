from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main(): #fills each column using helper functions
    turn_left()
    fill_column()
    next_column()
    fill_column()
    next_column()
    fill_column()
    next_column()
    fill_column()

def fill_column(): #fills a column with beepers and then returns to the initial spot
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    turn_around()
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()

def next_column(): #from the initial position, goes to the next column
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_right()
    turn_right()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
