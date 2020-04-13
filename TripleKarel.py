from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main(): #using helper functions, the main paints all three buildings
    paint_building()
    turn_right()
    paint_building()
    turn_right()
    paint_building()

def paint_side(): #paints a side of the building by putting a beeper in each spot while the front is clear
    while left_is_blocked():
        put_beeper()
        move()


def paint_building(): #uses paint_side to paint the three sides of the building
    paint_side()
    turn_left()
    move()
    paint_side()
    turn_left()
    move()
    paint_side()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
