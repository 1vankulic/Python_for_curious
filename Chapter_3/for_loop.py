# for redak in range(1, 11):
#     ispis_Retka = str()
    
#     for stupac in range(1, 11):
#         umnozak = redak + stupac
#         ispis_Retka += str.format("{0:<3}", umnozak)
#     print(ispis_Retka)
# print("\n" + "-" * 75)

for redak in range(1, 11):
    ispis_Retka = str()
    
    for stupac in range(1, redak + 1):
        umnozak = redak * stupac
        ispis_Retka += str.format("{0:>4}", umnozak)
    print(ispis_Retka)
print("\n" + "-" * 75)


for redak in range(1, 5):
    for stupac in range(1, 5):
        if stupac == redak:
            print(redak, stupac)
            break



