class Statistics:
    def __init__(self):
        self.numbers = [] #lista na liczby narazie pusta

    def add_number(self, number):
        self.numbers.append(number) #append dokleja liczbe na koniec listy

    def show_numbers(self):
        for number in self.numbers:
            print(number, end=" ") #wyswietlamy liczby oddzielone spacja
        print()

    def maximum(self):
        biggest = self.numbers[0] #zakladamy ze pierwsza liczba jest najwieksza
        for number in self.numbers:
            if number > biggest:
                biggest = number
        return biggest

    def minimum(self):
        smallest = self.numbers[0]
        for number in self.numbers:
            if number < smallest:
                smallest = number
        return smallest

    def avg(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        sorted_numbers = sorted(self.numbers)
        count = len(self.numbers) #ile mamy liczb
        middle = count // 2 #indeks naszej srodkowej liczby
        if count % 2 == 1:
            return sorted_numbers[middle] #przy nieparzystej ilości mediana to po prostu środkowa liczba
        return (sorted_numbers[middle-1] + sorted_numbers[middle]) / 2 #przy parzystej: średnia dwóch środkowych

    def show_statistics(self):
        print(f"Minimum: {self.minimum()}")
        print(f"Maximum: {self.maximum()}")
        print(f"Avg: {self.avg()}")
        print(f"Median: {self.median()}")
