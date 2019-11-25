## Elementi rjecnika nisu indeksirani i poredani vec im se pristupa neizmjenljivim kljucevima
## Svaki kljuc jedinstveno odreduje odgovarajuci element rjecnika, a vrijednosti mogu biti proizvoljni objekti

# Making a list
engHrv = {
    "alias": "inace zvan",
    "hash" : "sasjeckati"
}

# Getting value of a dictionary
engHrv["hash"] # sasjeckati
# engHrv[1] WON'T WORK 
# ---------------------------------------------------------------------------------------------------------- #
namirnice = {
    "cokolada": ["smede", "ukusno", "zdravo"],
    "kelj": ["zeleno", "izvrsno", "zdravo"],
    "luk": ["bijelo", "smrdljivo", "zdravo"],
    "spek": ["crveno", "njam", "nezdravo"]
}

namirnice["luk"]

# nove elemente dodajemo tako da dodamo kljuc koji ne vec ne postoji
namirnice["rajcica"] = ["crveno", "kiselkasto", "zdravo"]
# brisanje elementa
del namirnice['spek']
# ---------------------------------------------------------------------------------------------------------- #
tablica_1 = dict((["rajcica", "povrce"], ["jabuka", "voce"]))
tablica_2 = dict([("rajcica", "povrce"), ("jabuka", "voce")])
tablica_3 = dict(zip(["rajcica", "povrce"], ["jabuka", "voce"]))

print(tablica_1)
print(tablica_2)
print(tablica_3)
print("-" * 60)
# ---------------------------------------------------------------------------------------------------------- #
## Rjecnike s istom vrijednoscu u svim kljucevima mozemo stvarati pozivom clanske funkcije fromkeys.
## Ta funkcija u prvom argumentu prima niz kljuceva, a u drugom njihovu zajednicku vrijednost


tablica = dict.fromkeys(("rajcica", "luk"), "povrce")
print(tablica)
# ---------------------------------------------------------------------------------------------------------- #
nabava = {k: [] for k in ("rajcica", "luk")}
nabava['luk'].append('Sinisa')
nabava['rajcica'].append('Zoran')

print(nabava)


























