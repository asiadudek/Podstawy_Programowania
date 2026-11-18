#Wydatki miesięczne i odpowiadające im kategorie wydatków ujęte są w poniższych tablicach. 
#Napisz program, który oblicza, która kategoria wydatków była najdroższa.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

index_max = 0 #numer miejsca najwiekszego wydatku
for i in range(len(expenses)): #i to pozycja elementu, a len(expenses) to ilosc elementow tablicy expenses
    if expenses[i] > expenses[index_max]: #sprawdzamy czy wydatek na miejscu i jest wiekszy od dotychczasowego najwiekszego wydatku
        index_max = i #jesli warunek jest prawdziwy to nasze i staje sie pozycja najwieszego wydatku

print(categories[index_max], expenses[index_max])

