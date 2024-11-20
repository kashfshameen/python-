# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

################# Starter Code #####################
import random
Num_side:int=6
dice_1:int=random.randint(1,Num_side)

dice_2:int=random.randint(1,Num_side)
total:int=dice_2+dice_1
print("Dice have", Num_side, "sides each.")
print("First die:", dice_1)
print("Second die:", dice_2)
print("Total of two dice:", total)