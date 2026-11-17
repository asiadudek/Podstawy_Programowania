#Tekst zawiera dowolną liczbę słów. Zdefiniuj funkcje zwracającą akronim (pierwsze litery wszystkich słów)

def f(name):
    result = ""#puse miejsce do ktorego bedziemy wrzucac pierwsze litery wszystkich slow
    for char in name.split():# name.split() dzieli nam tekst na poszczegolne wyrazy osobno wiec przeszukujemy konkretne znaki wyrazow
        result = result + char[0]
    return result


name = input("Enter name: ")
print(f(name))
