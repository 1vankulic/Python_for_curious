voce = {"jagoda", "breskva", "rajcica"}
povrce = {"rajcica", "salata", "zelje"}
voce.union(povrce)
voce | povrce == voce.union(povrce)
# ----------------------------------------------------------------------------------------------------------------- #
voce.intersection(povrce)
voce & povrce
# ----------------------------------------------------------------------------------------------------------------- #
voce.difference(povrce)
povrce - voce
# ----------------------------------------------------------------------------------------------------------------- #
# Simetricnu razliku skupova dobivamo metodom symmetric_difference odnosno operatorom ^
# Rezultat ove operacije sadrzi elemente koji se pojavljuju u jednom od pocetnih skupova li ne u oba
ili_voce_ili_povrce = voce.symmetric_difference(povrce)
povrce ^ povrce
# ----------------------------------------------------------------------------------------------------------------- #
## MIJENJANJE I KOPIRANJE SKUPOVA
jelovnik = {"pizza", "samoborski kotlet", "varivo"}
jelovnik.add("rizoto") # add takes only one argument
jelovnik.update(["rizoto", "becki odrezak"])
jelovnik.update(["rizoto", "becki odrezak"])

# !! dodavanjem elemenata koji vec postoje u skupu nece imati nikakvog efekta te ce se zadrzati samo 1 vrijednost

jelovnik.remove("samoborski kotlet")
# ----------------------------------------------------------------------------------------------------------------- #

# remove uklanja element sa zadnom vrijednocu, a u slucaju da nema trazenog elementa vraca pogresku
# ako ne zelimo dojavu pogreske mozemo koristiti metodu discard
# pop uklanja slucajno izabrani element iz skupa i vrca njegovu vrijednost
# clear brise sve elemente iz skupa
# ----------------------------------------------------------------------------------------------------------------- #
## OBILAZENJE SKUPOVA
for blabla in jelovnik:
    print(blabla)
# ----------------------------------------------------------------------------------------------------------------- #
