glista = [1, 2, 3, 4, 5, 6]
max(glista)
min(glista)

osobe = [("Marko", 190, 105), ("Ivan", 180, 78), ("Rian", 190, 85)]
min(osobe) # Returns name that is highest alphabetically

# zelimo li usporediti osobu po masi 
import operator
dajMasu = operator.itemgetter(2) # gets 3rd element in each tuple
min(osobe, key=dajMasu)
max(osobe, key=operator.itemgetter(1, 2))

glista.index(max(glista))
glista.index(min(glista))
# ------------------------------------------------------------------------------------------------------------------ #
dajPrvog = operator.itemgetter(1) # dajPrvog vraca element na indeksu 1

cjenik = {
    'cevapi': 30,
    'grah': 20,
    'biftek': 70,
    'ramstek': 60
}
max(cjenik.items(), key=dajPrvog) # vraca jelo koje je najskuplje
# ------------------------------------------------------------------------------------------------------------------ #
## FUNKCIJA SUM
# sum takes at most 2 arguments
sum([1, 2, 3, 4, 5, 6, 4])

print(sum([[1, 2], [3, 1], [5, 1]], []))
# print(sum([1, 2], [3, 1], [5, 1])) 
# ------------------------------------------------------------------------------------------------------------------ #
import itertools

dekodiranaLista = [1, 1, 2, 3, 3, 3, 3]
podnizovi = itertools.groupby(dekodiranaLista)

for element, podlista in podnizovi:
    print(element, list(podlista))

glista1 = [1, 3, 4, 4, 5, 6, 8, 9, 9]
all(glista[i] <= glista[i+1] for i in range(len(glista) - 1))
# ------------------------------------------------------------------------------------------------------------------ #
## FUNKCIJA SORTED
L = list(range(5, -5, -1))
sorted(L)                        # [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
sorted(L, key=abs)               # [0, 1, -1, 2, -2, 3, -3, 4, -4, 5]
sorted(L, key=abs, reverse=True) # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]



































