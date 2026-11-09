###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
cuboid_volume = a * b * c #objetosc prostopadloscianu
cuboid_surface_area = 2*(a * b + b * c + a * c) #pole prostopadloscianu
print(f"The volume of cuboid volume is: {cuboid_volume}")
print(f"The surface area of cuboid is: {cuboid_surface_area}")