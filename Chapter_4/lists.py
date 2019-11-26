### Jedna od 2 slijedne kolekcije u Pythonu
### MUTABLE DATA STRUCTURE (object)

lista = []

sastojci = ["jaja", "brasno", "sol", "mlijeko", "marmelada"]
sastojci[4] = 'cokoladni namaz'

novi_sastojci = sastojci
# Both lists change their 5th item's value
novi_sastojci[4] = 'maslac od kikirikija'

## When copying lists you should do like this

novi_novi_sastojci = sastojci[:]
novi_novi_sastojci[4] = 'svjezi sir'

# novi_novi_sastojci = ["jaja", "brasno", "sol", "mlijeko", "svjezi sir"] 
# sastojci = ["jaja", "brasno", "sol", "mlijeko", "maslac od kikirikija"] 


## Another case
sastojci = novi_novi_sastojci
sastojci += ["rakija"]

# sastojci = ["jaja", "brasno", "sol", "mlijeko", "svjezi sir", "rakija"] 
# novi_novi_sastojci = ["jaja", "brasno", "sol", "mlijeko", "svjezi sir", "rakija"] 


## Same case with tuples
novi_novi_sastojci = tuple(sastojci[:-1])
# ("jaja", "brasno", "sol", "mlijeko", "svjezi sir")
sastojci = novi_novi_sastojci
sastojci += ("rakija",)
# sastojci = ("jaja", "brasno", "sol", "mlijeko", "svjezi sir", "rakija")
# novi_novi_sastojci = ("jaja", "brasno", "sol", "mlijeko", "svjezi sir")

# primjena operatora += nad n-torkom stvorila je novi objekt, u slucaju 
# izmjenljivog objekta postojeci se objekt prosiruje bez stvaranja kopije


## Stvaranje liste
lista = list("Python")

sastojcii = ["jaja", "brasno", "sol", "mlijeko", "marmelada"]
sastojci_na_m = [x for x in sastojcii if x[0] == "m"]
print(sastojci_na_m)