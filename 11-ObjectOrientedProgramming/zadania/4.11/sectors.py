from stadion import C

def main():
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})  # tworzymy obiekt stadionu z danymi(slownik)

    stadium.m1("G", 130) #zmieniamy liczbę fanów w sektorze G z 90 na 130
    print(stadium.m2("GD")) #sumuje G i D: 130 + 150 = 280
    print(stadium.m2("KEJ"))  # E i J nie istnieją, więc liczy się tylko K = 110

if __name__ == "__main__":
    main()