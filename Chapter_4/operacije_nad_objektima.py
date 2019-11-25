sastojci = ["jaja", "ulje", "sol"]

for x in sastojci:
    print(x)

for i in range(len(sastojci)):
    print(f"Na rednom broju {i} nalazimo {sastojci[i]}")

for i, x in enumerate(sastojci): # unumerate pobrojava vrijednosti liste 
    print(f"Na rednom broju {i} nalazimo {x}")
print("-"*60)

sastojci[2:4]

#------------------------------------------------------------------------
glista = [1, 2, 3, 4, 5]
glista[-2:] = [] # == del glista[-2:]
#------------------------------------------------------------------------
a, b, c = ('1', '2', '3')
x, y, z = '123'
#------------------------------------------------------------------------
prvi, *ostali = [1, 2, 3, 4, 5] 
# *(zvjezdicu) koristimo kada dodjeljujemo podatke liste, 
# varijabla koja ima * poprima vrijednosti ostatka podataka liste
ostali + [prvi] 
#------------------------------------------------------------------------
zamjena = ('cv', 'sm')
print(*zamjena)

zivotinja = "cvrcak"
zivotinja = zivotinja.replace(*zamjena)

if zamjena == (*zamjena,):
    print(1) # printat ce 1, isti su 
print(zivotinja)
#------------------------------------------------------------------------
raspon = range(0, 5)
print(raspon) #range(0, 5)
print(*raspon)