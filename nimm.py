"""
File: nimm.py
-------------------------
Add your comments here.
"""

def main():
    stones = 20
    player = 1
    while stones > 0:
        if player == 1:
            print("There are " + str(stones) + " stones left")
            choice = int(input("Player " + str(player) + " Would you like to remove 1 or 2 stones? "))
            if choice == 1:
                stones -=1
            elif choice == 2:
                stones -=2
            else:
                print("That is an incorrect choice. Please try again.")
            player +=1
        elif player == 2:
            print("There are " + str(stones) + " stones left")
            choice = int(input("Player " + str(player) + " Would you like to remove 1 or 2 stones?"))
            if choice == 1:
                stones -= 1
            elif choice == 2:
                stones -= 2
            else:
                print("That is an incorrect choice. Please try again.")
            player-=1
    print("Game over. Player " + str(player) + " won.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
