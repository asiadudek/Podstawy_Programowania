
import math

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

def triangle_area(a,b,c):
    s = (a + b + c) / 2 #s to polowa obwodu trojkata
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) #zastosowanie wzoru herona do obliczenia pola trojkata
    return area

print(f'The area of ​a triangle with sides {a},{b},{c} is {triangle_area(a,b,c)}')