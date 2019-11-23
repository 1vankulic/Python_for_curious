# 6. Provjerite je li zadani niz palindrom.
# - zanemariti razmake
# - zanemariti velika i mala slova

palindrom = str(input("Unesi recenicu za koju mislis da je palindrom\n"))

palindrom = palindrom.replace(" ", "")
palindrom = palindrom.lower()

print('-' * 80)
if palindrom[::-1] == palindrom:
    print('Recenica JE palindrom')
else:
    print('Recenica NIJE palindom')



