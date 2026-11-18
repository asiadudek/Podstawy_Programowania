#Utwórz program, który drukuje wszystkie unikalne elementy w tablicy. (czyli te co sie nie powtarzaja)
array = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:",array)
print("Unique elements: ", end=" ")
for x in array:
    if array.count(x) == 1: #jesli liczba wystepuje tylko raz to ja wypisujemy
        print(x, end=" ")