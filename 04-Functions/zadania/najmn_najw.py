
def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)



number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
number3 = int(input("Enter a number3: "))
print(f(number1, number2, number3))
