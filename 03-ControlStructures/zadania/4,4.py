###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#

university = "Krakow University of Economics"
university_expanded = "" #pusty napis do ktorego bedziemy dodawac znaki
for char in university:
    university_expanded = university_expanded + char + " " #czyli do naszej pustej zmiennej dodajemy znaki po kolei czyli litery ze spacjami między nimi

print(university)
print(university_expanded)