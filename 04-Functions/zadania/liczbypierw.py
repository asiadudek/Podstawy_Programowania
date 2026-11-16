def f(n):
    znaleziono = 0   # ile liczb pierwszych już znalazłam
    liczba = 1       # liczba, którą aktualnie sprawdzam

    while znaleziono < n:
        liczba = liczba + 1
        pierwsza = True

        for d in range(2, liczba):
            if liczba % d == 0:
                pierwsza = False

        if pierwsza:
            znaleziono = znaleziono + 1

    return liczba


n = int(input("Enter n: "))
print(f(n))