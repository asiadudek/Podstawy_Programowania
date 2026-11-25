import random

class Thermometer:
    def __init__(self):
        self.is_on = False #termometr wylaczony
        self.temperature = None #na start nie ma jeszcze pomiaru

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self): #funkcja zwracajaca pomiary, zapisuje wynik w atrybucie
        if self.is_on:
            self.temperature = round(random.uniform(38.0, 42.0),1) #uniform liczba z przecinkiem, round zaokragla do jednego miejsca
        else:
            print("Thermometer is off, turn it on")

    def show_temperature(self):
        if not self.is_on: #jesli termometr nie jest wlaczony
            print("Thermometer is off, turn it on")
        elif self.temperature >= 41.0:
            print(f"Temperature: {self.temperature}C (fever)")
            print("CRITICAL TEMPERATURE!!")
        elif self.temperature >= 37.0:
            print(f"Temperature: {self.temperature}C (fever)")
        else:
            print(f"Temperature: {self.temperature}C")