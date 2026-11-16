
def f(detector):
    in_room = 0
    for sign in detector:
        if sign =="+":
            in_room += 1
        else:
            in_room -= 1
        if in_room >= 3:
            return True
    return False

detector = input("Enter detector:")
print(f(detector))