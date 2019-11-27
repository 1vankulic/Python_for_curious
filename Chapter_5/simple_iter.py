L, w = [1, 2, 3], 3

# trazimo objekt w u listi L
for i, clan in enumerate(L):
    if clan == w:
        # print(f"Lista {L} sadrzi {w} na indeksu {i}")
        print("Lista", L, "sadrzi", w, "na indeksu", i)
        break
    else:
        print(f"Lista {L} ne sadrzi {w}")
# ------------------------------------------------------------------------------------------------------------------ #
## RASTAV NA PROSTE FAKTORE
n = int(input("Enter a number: \n"))

djelitelj = 2
import collections
rastav = collections.defaultdict(int)

while n > 1:
    while n % djelitelj == 0:
        rastav[djelitelj] += 1
        n /= djelitelj
    djelitelj += 1

print(rastav)