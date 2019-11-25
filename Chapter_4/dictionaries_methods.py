namirnice = {
    "rajcica": ["crveno", "kiselkasto", "zdravo"],
    "kelj": ["zeleno", "izvrsno", "zdravo"],
    "luk": ["bijelo", "smrdljivo", "zdravo"]
}

len(namirnice)
# when using in it is checking only keys, never values
"luk" in namirnice # True
"luk" in namirnice.keys()
"spek" in namirnice # False

zdraveNamirnice = [
    kljuc 
    for (kljuc, vrijednost) in namirnice.items()
        if 'zdravo' in vrijednost
]

print(zdraveNamirnice)
# -------------------------------------------------------------------------------------------------------- #
## Spajanje dvaju rjecnika provodimo metodom update
## Ta metoda sve lemente rjecnika zadanog argumentom dodjeljuje rjecniku nad kojim je metoda pozvana.
## Ako oba rjecnika imaju element s istim kljucem, dolazi do prepisivanja izvorne vriednosti novo vrijednoscu

nove_namirnice = {"jaja": ["narancasta", "ukusna", "zdravo"]}
namirnice.update(nove_namirnice)
nove_namirnice2 = {"jaja": ["jaja", "jaja", "jaja"]}
namirnice.update(nove_namirnice2)
# -------------------------------------------------------------------------------------------------------- #
## Kopiranje rjecnika
nove_namirnice = namirnice.copy()
nove_namirnice['rajcica'][0] = 'narancasto'
# -------------------------------------------------------------------------------------------------------- #
## Obilazenje rjecnika
for key in namirnice:
    print(f"Kljuc: {key}")
    print(f"Vrijednost: {namirnice[key]}")