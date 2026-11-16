###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    number = abs(number)
    text = str(number)
    total = 0

    for digit in text:
        total += int(digit)
    return total

number = int(input("Enter a number: "))
print(f"The sum of digits is: {sum_digits(number)}")