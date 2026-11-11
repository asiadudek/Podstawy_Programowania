

number = int(input("Enter number: "))
original_number = number 
result = "" #pusty napis, do niego kolejno będzie dopisywana reszta

if number == 0:
    result = 0 # jesli ktos wpisze liczbe "0" to pętla nie bedzie dzialac i liczenie od razu sie zakonczy

while number > 0: #petla wykona sie dopoki liczba bedzie wieksza od zera
    operation = number % 2 #reszta z dzielenia przez 2. Zawsze wyjdzie nam 0 albo 1. To jest nastepna cyfra liczby binarnej
    result = str(operation) + result #zamieniamy nasza reszte na typ str aby mozna bylo ja dodac do napisu. str(operation) to nasza nowsza cyfra a result pozostale cyfry reszty ktore byly obliczone wczesniej. program dodaje liczby tak aby powstala liczba binarna
    number = number // 2 #dzielimy nasza liczbe przez dwa bez reszty i zapisujemy ją jako liczba. czyli to nasza nowa liczba ktora rozpatrujemy. ona idzie na poczatek i wszystko od nowa. znowu liczymy reszte itd

print("Binary number:",result)