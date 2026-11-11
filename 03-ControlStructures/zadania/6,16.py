###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0 #calkowity czas prania
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n)') #dodatkowe plukanie
extra_spin = input('Extra spin? (y/n)') #dodatkowe wirowanie
washing_jacket = 40 #czas prania
washing_underwear = 70
washing_shoes = 20

if extra_spin == "y":
    extra_spin = 9
else:
    extra_spin = 0

if extra_rinse == "y":
    extra_rinse = 15
else:
    extra_rinse = 0

if program == "j":
    total_washing_time = washing_jacket + extra_spin + extra_rinse
elif program == "u":
    total_washing_time = washing_underwear + extra_spin + extra_rinse
else:
    total_washing_time = washing_shoes + extra_spin + extra_rinse

print(f"Total washing time: {total_washing_time} minutes.")