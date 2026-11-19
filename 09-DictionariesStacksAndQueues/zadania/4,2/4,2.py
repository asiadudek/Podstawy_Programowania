#napisz program, który zarządza kolejką plików do wydrukowania.
import queue

# creates a queue of files to print
files_to_print = queue.Queue()

while True:
   print('1. Add file to print')
   print('2. Print file')
   print('0. Quit')
   menu = input('Select an option: ')
   
   if menu == '1': #dodanie pliku do kolejki
      file_name = input('Enter file name to print: ') #nazwa pliku wpisana przez uzytkownika
      files_to_print.put(file_name) #put dodaje nazwe na koniec kolejki
      # add new file to the end of the queue 
   elif menu == '2': #drukowanie pliku
      if files_to_print.empty(): #jesli kolejka jest pusta
        print("Queue is empty")
      else:
        file_to_print = files_to_print.get()# print queue not empty
        print(f'File {file_to_print} is currently being printed. Please wait!')
   elif menu == '0':
      break