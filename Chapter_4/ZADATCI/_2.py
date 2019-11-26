# INVERTIRAJTE RJECNIK NA NACIN DA VRIJEDNOSTI POSTANU KLJUCEVI I OBRATNO 
# POD PRETPOSTAVKOM DA SU VRIJEDNOSTI JEDINSTVENE 

normal = {
    "ivan" : "ucenik",
    "marko": "profesor"
}

reversing_normal = {v: k for k, v in normal.items()}
print(reversing_normal)