# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works
import random

# Number of sides on each die to roll
NUM_SIDES = 6
def roll_dice():
     die1: int = random.randint(1, NUM_SIDES)
     die2: int = random.randint(1, NUM_SIDES)
     print("Die 1:", die1)
     print("Die 2:", die2)
     total=die1+die2
     print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

main()