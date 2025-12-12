computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()

i = 0

while i < len(computer_games):
    print(f"{i+1}. {computer_games[i]}")

    i += 1