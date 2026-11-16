def f(number1, number2, op):
    if op == "+":
        result = number1 + number2
    elif op == "-":
        result = number1 - number2
    elif op == "*":
        result = number1 * number2
    elif op == "**":
        result = number1 ** number2
    elif op == "%":
        result = number1 % number2
    else:
        result = None
    return result


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
op = input("Enter operator: ")
print(f(number1, number2, op))