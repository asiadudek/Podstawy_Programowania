#Napisz program wspierający obsługę klienta w biurze. Użyj kolejki. Każdy nowy klient otrzymuje bilet z automatycznie przypisanym kolejnym numerem 
#i jest dodawany na końcu kolejki. Następny obsługiwany klient jest pobierany od początku kolejki.


import queue

queue_1 = queue.Queue() #nasza kolejka, narazie jest pusta
ticket_number = 0  #numer ostatnio wydanego biletu, na start 0 (nikt jeszcze nie przyszedł)

while True: #petla bedzie sie wykonywac dopoki uzytkownik nie wybierze 3
    print("1. New customer")
    print("2. Serve next customer")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1": #nowy klient  
        ticket_number += 1 #kolejny numer biletu
        queue_1.put(ticket_number) #put dodaje bilet na koniec kolejki
        print("Your ticket number is: ",ticket_number)
    elif choice == '2': #obsluga nastepnego klienta
        if queue_1.empty(): #true - jesli nikogo w kolejce nie ma
            print("Queue is empty")
        else: #jesli ktos jest w kolejce
            customer = queue_1.get() #get zdejmuje bilet z poczatku kolejki (najdluzej czekajacy)
            print("Now serving customer number", customer) #wypisuje numer obslugiwanego klienta
    elif choice == '3':
        break


