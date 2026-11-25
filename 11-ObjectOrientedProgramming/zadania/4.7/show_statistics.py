from statystyka import Statistics

def main():
    stats = Statistics() #obiekt narazie z pusta lista liczb

    # dodajemy liczby z zadania (zamiast wpisywać je z klawiatury)
    stats.add_number(12)
    stats.add_number(37)
    stats.add_number(6)
    stats.add_number(9)
    stats.add_number(17)

    stats.show_numbers()        # wszystkie liczby
    stats.show_statistics()     # min, max, średnia, mediana


if __name__ == "__main__":
    main()