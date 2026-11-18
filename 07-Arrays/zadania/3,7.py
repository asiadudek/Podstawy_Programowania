#Utwórz program, który drukuje najdłuższą nazwę (składającą się z największej liczby znaków)

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = names[0] #przyjmujemy ze najdluzsza nazwa znajduje sie na 1 miejscu
for name in names: #przeszukujemy wszystkie imiona z tablicy
    if len(name) > len(longest): #jesli dlugosc sprawdzanego imienia jest dluzsza od naszego najdluzszego
        longest = name #to najduzsze imie staje sie teraz naszym imieniem ktore sprawdzalismy

print("Names:",names)
print("Longest name:",longest)