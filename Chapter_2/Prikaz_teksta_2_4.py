len("pro" + "ba") # 5
s = "probni niz"
s[5] # i
s[-1] # z

niz = "Proba izrezivanja podniza."
niz[6:11] # 'izrez'

number_niz = "1234567890"
niz[1:9:2] # [pocetak:kraj:iteracija]
# '2468'

number_niz[:] # 1234567890

number_niz[::-1] # reversing a string

"x" in "smrčak" # False
"č" in "cvrčak" # True
"č" not in "krčak" # False

2 in (1, 2, 3) # True

"krk" in "čekrk" # True
"krk" in "korak" # False

znakovni_niz = "    Zeko i potocic    "
b = znakovni_niz.strip()
znakovni_niz.upper()
znakovni_niz.lower()


"zeko".islower() # True
"ZEKO".isupper() # True
"ZEKo".isupper() # False

"zeko".isalpha() # Returns True if ALL chars are alphabet chars
"123".isdigit() # Returns True if ALL chars are numbers

"marama".count("ma") # 2
"marama".find("ar") # na kojem polozaju se javlja "ar", polozaj 1
"marama".find("xx") # -1


"kolotura".startswith("kolo") # True

znakovni_niz2 = "Niz: jabuka kruška jagoda jabuka"
znakovni_niz2.replace("jabuka", "trešnja") # replace(string koji se mijenja, novi string)

opis = "Marko; Markovic; M; 1981; programer"
print(opis.split(";"))







