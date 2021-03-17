# List teman yuki sebanyak 10
chingu = ['Novela', 'Arum','Exga','tazkiya','Diva', 'Nina', 'Namira','Afnia', 'Iffa', 'Nindya']

# menampilakan list indeks nomor 4,6,7
print(chingu[4], chingu[6], chingu[7])

#Mengganti list 3,5,9
chingu[2] = 'Rika'
chingu[4] = 'Ramadhani'
chingu[8] = 'Anggar'

print(chingu)

# Menambah 2 teman yuki pada list
chingu.extend(["Falda", "piero"])

print(chingu)

# Menampilkan semua teman yuki dengan perulangan
print( chingu * 5)
# Menampilkan Panjang list
print(len(chingu))