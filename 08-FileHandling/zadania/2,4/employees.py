###
# Saves to a file a list of employees working at a specified position.
#Napisz program, który zapisuje dane pracowników zatrudnionych na stanowisku 'Inżynier oprogramowania'

# file names
original_file = 'it_company.csv'
target_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(original_file, 'r') as input_file: #czyli otwórz plik jako plik wejściowy do czytania
   with open(target_file, 'w') as output_file: #czyli utwórz lub otwórz plik wyjściowy, gotowy do zapisu danych
      for line in input_file: #sprawdzamy czy napis zawarty w job_title wystepuje gdzies wewnatrz wiersza/linii
         if job_title in line:
            output_file.write(line) #jesli jest to wypisujemy go do pliku wyjsciowego