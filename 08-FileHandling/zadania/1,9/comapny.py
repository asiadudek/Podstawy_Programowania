###
# Prints employees employed in a specified position.
# Napisz program, który wyświetla tylko pracowników ze stanowiskiem "Inżynier oprogramowania". Numeruj pozycje na drukowanej liście.

# Employee List
file_name = 'it_company.csv' #nazwa pliku z danymi wszystkich pracowników

# Position
job_title = 'Software Engineer' #szukane stanowisko (napis, którego szukamy w każdej linii)

counter = 1 #licznik
with open(file_name, 'r') as file:
   for line in file:
      if job_title in line: 
        print(counter, line, end='') #wypisujemy go razem z numerem
        counter  += 1 #po sprawdzeniu danej linii i znalezieniu takiego tytulu zwiekszamy licznik o 1