#Napisz program, który sprawdza, czy pierwsza tablica jest podzbiorem drugiej 
#(czy wszystkie elementy pierwszej tablicy pojawiają się w drugiej tablicy).

first = [2, 5, 7] 
second = [1, 2, 3, 5, 7, 9] 

is_subset = True # wynik, zakladamy "tak" dopoki nie znajdziemy roznicy (czy jest podzbiorem)
for x in first: #sprawdzamy element x first
    found = False #zakladamy ze nie znalezlismy. "Czy jest w second?"
    for y in second: #sprawdzamy element z second
        if x == y: #warunek ktory musi byc spelniony zeby bylo True
            found = True 
    if not found: #jesli nie sa rowne to first nie jest pozdbiorem
        is_subset = False

print("First array: ", first)
print("Second array: ",second)

if is_subset:
    print("Result: the first array is a subset of the second")
else:
    print("Result: the first array is not a subset of the second")