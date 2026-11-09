###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

swift = input("Enter SWIFT code: ")
print(f"Bank code: {swift[0:4]}") #ostatni znak się nie wlicza więc musimy o jeden wiecej
print(f"Country Code: {swift[4:6]}")