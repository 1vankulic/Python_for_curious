## Iteratori se koriste za prolazak kroz vrijednost kolekcija

jezici = ('kineski', 'spanjolski', 'engleski')
it = iter(jezici)

for x in it:
    print(x, end=' ')

for x in reversed(range(10)): print(x, end=' ')
# ---------------------------------------------------------------------------------------------------------------
drzave = ['Kina', 'SAD', 'Indija']

it = iter(drzave)

next(it)

try:
    while True:
        x = next(it)
        print(x)
except StopIteration:
    pass
# ---------------------------------------------------------------------------------------------------------------
## PREOKRETANJE NIZOVA
glista = ['Marko', 'Mislav', 'Jagor']

print(''.join(reversed(glista[0])))
print(*reversed(glista))
## GENERATORSKI IZRAZI 
# Generatori su specijalna vrata iteratora koje stvaramo generatorskim gunkcijama ili generatorskim izrazima

import itertools

g = (x**2 for x in itertools.count(1) if x%2 == 1)
