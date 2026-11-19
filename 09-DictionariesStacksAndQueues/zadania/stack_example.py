
"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
numbers = []

# adds elements to the top of the stack
numbers.append(2)
numbers.append(3)
numbers.append(7)
numbers.append(4)
numbers.append(1)
numbers.append(9)
numbers.append(8)

## sumujemy dwie ostatnie cyfry stosu
print("Total:",numbers[-2] + numbers[-1])

#liczymy sumę pozostalych elementow stosu
total = 0
while len(numbers) > 0:
    total += numbers.pop()
print("Total of the rest:",total)

"""
Note the order of the printed elements.
The last added element is printed first.
"""