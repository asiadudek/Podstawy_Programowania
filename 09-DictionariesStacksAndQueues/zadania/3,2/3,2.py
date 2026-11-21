#symulacja klawisza wstecz

# create a visited_websites
visited_websites = [] #stos odwiedzonych stron, na start pusty

#strony odwiedzone wcześniej; append kładzie stronę na wierzch stosu
visited_websites.append('instagram.com')
visited_websites.append('uek.krakow.pl')
visited_websites.append('microsoft.com')

while True: #petla dziala az zatrzyma ja break
   website = input('Enter website name (0 for back): ')

   if website == '0':
      if visited_websites == 0: #nie ma juz gdzie wracac, kolejka jest pusta
         break 
      else:
         print('<-- Going back to a previously visited website')
         website = visited_websites.pop() 
   elif website != "": #jesli uzytkownik wpisal cos innego niż 0 to tworzymy nową strone
      visited_websites.append(website) #kladzie nowa strone na wierzch stosu


   print('You are currently viewing:', website)
   print()
