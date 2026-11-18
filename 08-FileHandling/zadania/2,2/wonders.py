###
# Writes Seven Wonders of the World to a file
#Napisz program, który zapisuje listę Siedmiu Cudów Świata do pliku tekstowego, 
#w kolejności alfabetycznej, z każdą nazwą w osobnym wierszu. 


seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt' #nazwa pliku do ktorego zapiszemy liste

# Sort data alphabetically
seven_wonders = sorted(seven_wonders) #sortujemy nasze dane

# Write data to the file
with open(file_name, 'w') as file:
      for item in seven_wonders: #przeszukujemy nasza liste
        file.write(item + '\n') #wypisujemy elementy listy w nowych wierszach i zapisujemy w nowym pliku