#Prawidłowe hasło powinno składać się z co najmniej sześciu znaków, a każdy znak pojawia się w haśle tylko raz.
#Zdefiniuj funkcje która zwraca wartość True, jeśli hasło jest poprawne, lub False w przeciwnym wypadku.
def f(password):
    if len(password) < 6: #jesli dlugosc hasla jest mniejsza od 6
        return False #zwracamy false
    for char in password: #przeszukujemy kazdy znak, litere w podanym przez uzytkownika hasle
        if password.count(char) > 1: #jesli znak w tekscie powtarza sie wiecej niz raz
            return False #zwracamy false
    return True 


password = input("Enter password: ")
print("Correct password:",f(password))