import time as time

# Wneljae

time_delay = [4.6, 4.9, 4.5, 4.8, 3.9, 4.6, 4.5, 4.2, 2.2, 4.5, 4.8, 4.6, 4.5]
lyrics = ["Hindi na makalaya", 
          "Dinadalaw mo 'ko bawat gabi", 
          "Wala mang nakikita", 
          "Haplos mo'y ramdam pa rin sa dilim", 
          "Hindi na na-nanaginip", 
          "Hindi na ma-makagising",
          "Pasindi na ng ilaw",
          "Minumulto na 'ko ng damdamin ko",
          "Ng damdamin ko",
          "'Di mo ba ako lilisanin?",
          "Hindi pa ba sapat pagpapahirap sa 'kin?",
          "Hindi na ba ma-mamamayapa?",
          "Hindi na ba ma-mamamayapa?"]


lyrics_lenght = len(lyrics)

for i in range(lyrics_lenght):
    print(f"{lyrics[i]}")
    time.sleep(time_delay[i])

print("\nWneljae")
