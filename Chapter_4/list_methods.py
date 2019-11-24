sastojci = ["jaja", "brasno", "sol", "mlijeko"]

sastojci.append("cokoladni sirup") # (append) dodaje proslijedenu vrijednost na kraj liste
sastojci.insert(2, "pekmez")       # (insert) umece proslijedenu vrijednost na poziciju zadanu indeksom
sastojci.index("mlijeko")          # (index) vraca indeks prve pojave proslijedene vrijednosti u listi
sastojci.remove("pekmez")          # (remove) iz liste brise prvu pojavu proslijedene vrijednosti
sastojci.reverse()                 # (reverse) obrce redoslijed elemenata
sastojci.sort()                    # (sort) sortira elemente liste
sastojci.pop()                     # (pop) brise element zadan indeksom iz liste, bez indeksa brise zadnji
sastojci.pop(2)                    # (count) vraca broj pojavljivanja zadanog elementa u listi
sastojci.count("mlijeko")

# ---------------------------------------------------------------------------------------------------------------
##  liste  za kolekcije istovrsnih elemenata
## n-torke za kolekcije raznovrsnih elemenata

osobe = [
    ("Marko", 190, 105),
    ("Ivan", 180, 98),
    ("Hrvoje", 190, 85)
]

ukupnaMasa = 0
for x in osobe:
    ukupnaMasa += x[2]
print(f"Prosjecna masa je: {ukupnaMasa / len(osobe)} kg")





