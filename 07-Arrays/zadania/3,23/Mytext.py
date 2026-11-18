
def count_words(text):
    count = 0 #licznik slow
    in_word = False #czy aktualnie jestesmy w srodku slowa, zakladamy ze nie
    for char in text: #char to aktualna litera bądź spacja z tekstu
        if char != " ": # jesli jestesmy na literze i to litera a nie spacja
            if not in_word: #jesli nie jestesmy jeszcze w srodku slowa
                count += 1 #zwiekszamy nasz licznik o 1
            in_word = True #od teraz jestesmy w slowie, kolejne litery nie zwieksza licznika
        else: #jesli znak jest spacja
            in_word = False
    return count
        

def word(text): #lista naszych slow
    n = count_words(text) #ile mamy slow w tekscie, zliczamy
    words = [""] * n #mnozymy nasze miejsce gdzie bedziemy przechowywac slowa przez ilosc slow ktore policzylismy
    index = 0 #numer slowa ktore teraz tworzymy
    in_word = False #czy jestesmy w srodku slowa
    for char in text: #przechodzimy po wszystkich znakach w tekscie
        if char != " ":
            words[index] += char #doklejamy litere aktualnego slowa do naszej listy
            in_word = True #jestesmy w slowie
        else: #jesli znak jest spacja
            if in_word: #jesli nie jestesmy juz w slowie bo mamy spacje
                index += 1 #zwiekszamy nasz index czyli pozycje i przechodzimy do nastepnego slowa
            in_word = False #nie jestesmy juz w slowie
    return words

def length_words(text):
    words = word(text) #nasze slowa do posortowania
    n = len(words) #liczba slow
    for i in range(n-1): #tyle razy ma sie powtorzyc petla ile slow
        for j in range(n-1-i): #porownujemy pary sasiadow, j to numer slowa po lewej stronie, liczba par (n-1) minus liczba miejsc ktore są juz gotowe na koncu
            if len(words[j]) < len(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return words

def words_alphabetically(text):
    words = word(text) #nasze slowa do wyswietlenia
    n = len(words) #liczba slow
    for i in range(n-1): #petla powtorzy sie tyle ile mamy naszych slow
        for j in range(n-1-i): #j to pozycja slowa po lewej stronie
            if words[j].lower() > words[j+1].lower(): #żeby wielkosc liter nie psula kolejnosci
                words[j], words[j+1] = words[j+1], words[j]
    return words