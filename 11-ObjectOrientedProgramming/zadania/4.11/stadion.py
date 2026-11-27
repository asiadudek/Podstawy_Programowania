class C:
    def __init__(self, sectors): #konstruktor, uruchamia sie automatycznie przy tworzeniu obiektu
        self.sectors = sectors #zapisujemy nasz slownik w obiekcie

    def m1(self, s, n): #s to litera sektora, n to liczba fanow, metoda zmieniajaca liczbe fanow w sektorze
        self.sectors[s] = n #jesli sektor istnieje, zamienia liczbe, jesli nie to dodaje nowy sektor

    def m2(self, s): # s to ciag liter, zwraca sume fanow w sektorach
        total = 0 #suma fanow
        for letter in s: #bierzemy po kolei kazda litere z ciagu
            if letter in self.sectors: #sprawdzamy czy taki sektor istnieje na stadionie
                total += self.sectors[letter] #jesli tak to dodajemy jego fanow do sumy
        return total