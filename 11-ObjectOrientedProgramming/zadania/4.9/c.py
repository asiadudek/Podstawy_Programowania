#ciąg zawierajacy nazwisko, pierwsza litere imienia i ile lat przepracowanych
class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority #staz pracy

    def __str__(self): #metoda specjalna, ktora pokazuje jak nasz obiekt wyglada jako tekst
        text = self.surname + self.name[0] + str(self.seniority)
        if self.age >= 18:
            return text.upper()
        return text.lower()