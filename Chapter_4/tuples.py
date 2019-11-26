# Jedna od 2 slijedne kolekcije u Pythonu
# IMMUTABLE DATA STRUCTURE

# varijabla = (podatci)
# npr
# stol = ("mis", 120cm, "laptop")


# Stvaranje N-torke
osobaA = ()
# Popunjavanje N-torke
osobaA = ("Strahimir", "Desnica", 120, False)

ntorka = tuple("proba") 
# ('p', 'r', 'o', 'b', 'a')


# a = (1) error must be written like on line 19
a = (1,)
print(type(a))


# Same things
x = 'kevapi', 20
y = ('kevapi', 20)


x = 2 * (1, 2) + (3, 4)
x += 1
x.count(1) # Izbacuje broj jedinica
x.index(2) # Izbacuje mjesto dvojkes
