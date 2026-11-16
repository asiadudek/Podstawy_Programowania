
def input_boolean(number, even):
    total = 0

    for digit in str(number):
        digit = int(digit)
        if even == True:
            if digit % 2 == 0:
                total = total + digit
        else:
            if digit % 2 != 0:
                total = total + digit

    return total
    

number = input("Enter the number: ")
even = input("Summation of even digits? (True/False): ")
if even == "True":
    even = True
else:
    even = False

print(input_boolean(number, even))
