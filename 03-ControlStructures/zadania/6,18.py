

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    coordinate = "first quadrant" #cwiartka pierwsza
elif x < 0 and y > 0:
    coordinate = "second quadrant"
elif x < 0 and y < 0:
    coordinate = "third quadrant"
elif x > 0 and y < 0:
    coordinate = "fourth quadrant"
else:
    coordinate = "position (0,0)"


print(f"Point P({x},{y}) is in the {coordinate} of the coordinate system")