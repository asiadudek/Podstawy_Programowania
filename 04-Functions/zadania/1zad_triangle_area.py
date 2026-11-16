
import math

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

def triangle_area(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print(f'The area of ​a triangle with sides {a},{b},{c} is {triangle_area(a,b,c)}')