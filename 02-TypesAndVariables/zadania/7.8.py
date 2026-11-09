###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll1 = random.randint(1,6) #dice roll - rzut kostka
dice_roll2 = random.randint(1,6)
dice_roll3 = random.randint(1,6)
print(f"Dice roll 1: {dice_roll1}")
print(f"Dice roll 2: {dice_roll2}")
print(f"Dice roll 3: {dice_roll3}")
total = dice_roll1 + dice_roll2 + dice_roll3
print(f"Total: {total}")