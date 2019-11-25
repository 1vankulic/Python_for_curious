tekst = """ Jedna je macka zivjela sama
            u svome stanu, kao dama,
            i tamo joj je bilo krasno;
        """

# histogram slova
import string
zaIzbaciti = string.whitespace + string.punctuation
tekst = tekst.translate(str.maketrans('', '', zaIzbaciti)).lower()
print(tekst)

histogram = {slovo: tekst.count(slovo) for slovo in set(tekst)}
print(histogram)