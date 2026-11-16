

def f(n):
    total = ""
    
    for char in range(n):
        if n > 1:
            total = total + "*" + "/"
        else:
            total = total + "*"
    return total

n = int(input("Enter number: "))
print(f(n))