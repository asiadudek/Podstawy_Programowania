
def f(expression):
    result = 0
    operator = "+"
    for char in expression:
        if char == "+" or char == "-":
            operator = char
        else:
            cyfra = int(char)
            if operator == "+":
                result = result + char
            else:
                result = result - char
    return result


expression = input("Enter expression: ")
print(f(expression))