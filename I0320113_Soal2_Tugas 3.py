dict = {
    "nama": "Yuki Rizkylawati",
    "hobi": ["Nonton drama","Mendengarkan musik","Dance"],
    "sosmed" : { 
        "instagram": "yukirizky_",
        "twitter": "yukirizkylawati",
        "line": "yukirizky12"
        },
    "lagu" : ["running", "yours","celebrity"],
    "makanan" : ["kebab","nasi","ayam goreng"]
    }

# menampilkan salah satu nilai dari key
print("Nama : %s" % dict["nama"])
print("hobi : %s"% dict["hobi"][1])
print("Sosial media: %s"% dict["sosmed"]["instagram"])
print("lagu favorit: %s"% dict["lagu"][0])
print("Makanan favorit: %s"% dict["makanan"][2])

# Mengubah salah satu hobi dan sosial media
dict["hobi"][0] = "Bersih-bersih"
dict["sosmed"]["instagram"] = "rzky.ly"

print(dict)

# Menghapus 2 makanan favorit
del dict ["makanan"][0]
del dict ["makanan"][1]

print(dict)

# Menambahkan satu hobi
dict["hobi2"] = "Mancing"

print(dict)
