
#funkcja sprawdzajaca czy podana liczba binarna jest prawidlowa
def input_boolean(binary_number):
    for digit in binary_number:
        if digit != "0" and digit != "1":
            return False
    else:
        return True


binary_number = input("Enter binary number: ")
print(input_boolean(binary_number))