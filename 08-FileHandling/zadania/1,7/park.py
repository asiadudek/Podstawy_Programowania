###
# Reads the entire contents of a file
#Wypełnij poniższy program, aby obliczyć całkowitą liczbę zaparkowanych samochodów.

def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read() #cala zawartosc pliku, jeden napis
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt') #cała zawartość car_park.txt jako jeden napis
file_lines = file_content.splitlines() #dzielimy nasz tekst na linie/wiersze

# calculates the total number of cars parked
total = 0 #suma aut zaparkowanych
for line in file_lines:
   total += int(line)

print('Total cars parked:', total)