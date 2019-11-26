## Asocijativna kolekcija u kojoj su vrijednosti ujedno i kljucevi
## Skupove cemo tipicno uportrebljavati za uklanjanje visetrukih elemenata iz slijednih kolekcija,
## izuzetno brzo ispitivanje pripadnosti, te u slucajevima kad nam usrebaju 
## skupovne operacije poput unije ili presjeka

jelovnik = {"pizza", "samoborski kotlet", "varivo"}

# pripadnost
"samoborski kotlet" in jelovnik
"salata" in jelovnik

print({"samoborski kotlet", "salata"}.issubset(jelovnik))
# .issubset returns true if all items of compared lists are in the list we are comparing 
print({"samoborski kotlet", "varivo"} <= jelovnik)

# ----------------------------------------------------------------------------------------------------------------- #
# .issuperset returns True if all items in the specified set exists in the original set, otherwise it retuns False
print({"samoborski kotlet", "salata"}.issuperset(jelovnik))
print(jelovnik >= {"samoborski kotlet", "varivo"} )
# ----------------------------------------------------------------------------------------------------------------- #
# vraca istinu ako maticni skup nema zajednickih elemenata sa skupom iz argumenta
not jelovnik.isdisjoint({"becki odrezak", "varivo", "rizoto", "juha", "pizza", "kajgana"})
# ----------------------------------------------------------------------------------------------------------------- #
## Stvaranje skupova
set(range(10)) # {0,1,2,3,4,5,6,7,8,9}

nizovi = {list, tuple, range, str, bytes, bytearray}
sorted([x.__name__ for x in nizovi])





















