tekst = """ Jedna je macka zivjela sama
            u svome stanu, kao dama,
            i tamo joj je bilo krasno;
        """

# histogram slova
import string
zaIzbaciti = string.whitespace + string.punctuation
tekst = tekst.translate(str.maketrans('', '', zaIzbaciti)).lower()
print(tekst)

histogram = {slovo: tekst.count(slovo) for slovo in set(tekst)}
print(histogram)
# ---------------------------------------------------------------------------------------------------------------
osobe = ["marko", "ana", "ivica"]

for i, ime in enumerate(osobe):
    osobe[i] = ime[0].upper() + ime[1:0]
# ---------------------------------------------------------------------------------------------------------------
# IZMJENA ELEMENATA RJECNIKA

cjenik = {
    'cevapi': 30,
    'raznjici': 35
}

for x, y in cjenik.items():
    cjenik[x] = round(y**0.8)
# ---------------------------------------------------------------------------------------------------------------
import collections

Osoba = collections.namedtuple('Osoba', 'ime prezime godina')

o = Osoba("Ivo", "Peric", 1971)
# ---------------------------------------------------------------------------------------------------------------
## REDOVI
red = collections.deque([1, 2, 3])
red.append(4); red.appendleft(5)
print(red)

x = red.pop(); z = red.popleft();
print(x, z) # (4, 5)

red.rotate(2)
# ---------------------------------------------------------------------------------------------------------------
## VARIJANTE RJECNIKA
c = collections.Counter("abrakadabra") # pobrojavanje ucestalosti elemenata
c.most_common(1)