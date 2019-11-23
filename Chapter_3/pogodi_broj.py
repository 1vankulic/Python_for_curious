import random

najmanji = 1
najveci = 100

print(f"Pogodi broj izmedu {najmanji} i {najveci}")
random.seed()

brojKojiPogadamo = random.randint(najmanji, najveci)
brojJePogoden = False
brojPokusaja = 0

while not brojJePogoden:
    broj = int(input("Upisi pretpostavljeni broj: "))
    brojPokusaja += 1

    if broj > brojKojiPogadamo:
        print("Manji je od toga")
    elif broj < brojKojiPogadamo:
        print("Veci je od toga")
    else:
        print(f"Bravo, pogodio si u {brojPokusaja} pokusaja")
        brojJePogoden = True