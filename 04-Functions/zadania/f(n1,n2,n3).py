

def input_boolean(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False

n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))
n3 = int(input("Enter a number n3: "))
print(input_boolean(n1,n2,n3))