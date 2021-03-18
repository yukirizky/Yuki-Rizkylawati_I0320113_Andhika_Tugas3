# List teman yuki sebanyak 10
chingu = ['Novela', 'Arum','Exga','tazkiya','Diva', 'Nina', 'Namira','Afnia', 'Iffa', 'Nindya']

# menampilakan list indeks nomor 4,6,7
print(chingu[4], chingu[6], chingu[7])

#Mengganti list 3,5,9
chingu[3] = 'Rika'
chingu[5] = 'Ramadhani'
chingu[9] = 'Anggar'

print(chingu)

# Menambah 2 teman yuki pada list
chingu.extend(["Falda", "piero"])

print(chingu)

# Menampilkan semua teman yuki dengan perulangan
print ("Teman yuki : ada {} orang".format (len(chingu)))
for teman in chingu:
    print (teman)
    
# Menampilkan Panjang list
print(len(chingu))
