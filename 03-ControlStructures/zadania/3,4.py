###
# Checks whether at least one number entered
# from the keyboard is not negative
# 

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if not x < 0 or not y < 0: # jesli x nie jest ujemne lub y nie jest ujemne. Not nam odwraca dany warunek
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f"Both numbers are negative.")