

def f(x,y):
    total = 0

    for number in range(x,y+1):
        if number < 0 and number >= x and number <= y:
            if number % 2 == 0:
                total = total + 1
    return total

    
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f(x,y))