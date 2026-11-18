computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
game = 0 #nasz indeks aktualnej gry
sorted = sorted(computer_games) #sortujemy alfabetycznie nasze gry z listy
while game < len(sorted): #petla bedzie sie wykonywac dopoki indeks gry jest mniejszy od indeksu osttaniej gry
    print(game + 1, sorted[game]) #wyswietlamy indeks i nazwe gry
    game += 1

