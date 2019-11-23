# while True:
#     unos = input("Upisi pretpostavljeni broj: ")
#     if unos.isnumeric() == False:
#         print("Treba unijeti broj!")
#         continue

## do while in python


# import random

# random.seed()
# sestica_bacena = False

# for x in range(3):
#     if random.randint(1, 6) == 6:
#         print("Bacena je sestica")
#         sestica_bacena = True
#         break
# if not sestica_bacena:
#     print("Sestica nije bacena")

## Simpler way 

import random

sestica_bacena = random.randint(1, 6) == 6

while True:
    if sestica_bacena == True:
        print("Sestica je bacena")
        break
    else:
        print("Sestica nije bacena")