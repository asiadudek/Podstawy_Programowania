

def f(product_code):
    result = 0
    for i in range(3):
        result = result + int(product_code[i])
    rest = result % 7
    return rest == int(product_code[3])


product_code = input("Enter product code: ")
print(f(product_code))