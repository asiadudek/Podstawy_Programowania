#Zdefiniuj funkcje, która zwraca podany tekst ze wszystkimi znakami oddzielonymi znakiem myślnika.
def f(text):
    result = "" #puste miejsce na nasz tekst po zmianie
    for char in range(len(text)):
        if char > 0: #jesli znak nie stoi na 1 pozycji
            result = result + "-" #to najpierw dopisujemy myslnik
        result = result + text[char] #a potem dopisujemy znak ktory stoi na pozycji char
    return result


text = input("Enter text: ")
print(f(text))