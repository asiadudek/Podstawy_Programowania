#symulacja klawisza wstecz
import queue

# create a visited_websites
visited_websites = queue.LifoQueue() #stos odwiedzonych stron, na start pusty

#strony odwiedzone wcześniej; put kładzie stronę na wierzch stosu
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True: #petla dziala az zatrzyma ja break
   website = input('Enter website name (0 for back): ')

   if website == '0':
      if visited_websites.empty(): #nie ma juz gdzie wracac, kolejka jest pusta
         break #konczymy
      else:
         print('<-- Going back to a previously visited website')
         website = visited_websites.get() #get - zdejmuje ze stosu stronę z WIERZCHU (ostatnio dodaną)
   elif website != "": #jesli uzytkownik wpisal cos innego niż 0 to tworzymy nową strone
      visited_websites.put(website) #kladzie nowa strone na wierzch stosu

   # print name of website you are currently viewing
   print('You are currently viewing:', website)
   print()
