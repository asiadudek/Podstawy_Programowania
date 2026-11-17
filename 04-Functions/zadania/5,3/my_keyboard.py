###
# Functions to read any data type from the keyboard
#

def input_string(message): #funkcja zwraca ciag znakow wprowadzonych z klawiatury
    value = input(message)
    return value

def input_integer(message): #funkcja zwraca liczbe calkowita wprowadzona z klawiatury
    value = input(message) #funkcja pobiera tekst i zapisuje go w zmiennej value
    return int(value)

def input_real(message): #funkcja zwraca liczbe rzeczywista wprowadzona z klawiatury
    value = input(message)
    return float(value)

def input_boolean(message): #funkcja zwraca wartosc logiczna wprowadzona z klawiatury
    value = input(message)
    return value == 'y' #jesli wpisano y to funkcja zwraca true, w przeciwnym razie zwraca False



