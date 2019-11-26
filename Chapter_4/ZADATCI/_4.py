# Napisite kod za pretvaranje zadane recenice u CamelCase oblik
# npr. "prva druga"
# treba prevesti u 
# "PrvaDruga"

import string

sentence = input("Enter a sentence: \n")

sentence_splitted = sentence.split()

result = ""

for word in sentence_splitted:
    word = word.capitalize()
    result += word

print(result)
