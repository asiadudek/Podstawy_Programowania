###
# Makes a copy of a text file

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt' #nasz docelowy plik

# read the content of the original file
with open(original_file, 'r') as file:
   content = file.read() #wczytujemy zawartosc pliku

# write the content to the target file (copy)
with open(target_file, 'w') as file:
   file.write(content) #zapisujemy zawartosc pliku oryginalnego do kopii