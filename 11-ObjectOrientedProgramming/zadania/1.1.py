#zmodyfikuj klasę, dodając trzeci atrybut. Następnie wprowadź zmiany w programie, dodając trzeciego ucznia

# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.city = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()

    student1.name = "Dominic"
    student1.age = 19
    student1.city = "Krakow"

    student2.name = "Olivia"
    student2.age = 21
    student2.city = "Wieliczka"
    
    student3.name = "David"
    student3.age = 18
    student3.city = "Tarnow"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, city: {student1.city}')
    print(f'{student2.name}, {student2.age} years old, city: {student2.city}')
    print(f'{student3.name}, {student3.age} years old, city: {student3.city}')

if __name__ == "__main__": #ten warunek sprawdza czy plik zostal uruchomiony bezposrednio, jesli tak to sie uruchamia
    main()