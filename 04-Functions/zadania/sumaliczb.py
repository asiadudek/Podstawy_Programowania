
def f(x,y):
    result = 0
    for i in range (x, y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            result = result + i
    return result




x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f(x,y))