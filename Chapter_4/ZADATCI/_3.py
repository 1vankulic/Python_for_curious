# Napiste izraz za preplitanje triju pobrojivih objekata
# npr. preplitanjem 
# range(2), "ab", (8, 9)
# trebalo bi dobiti listu
# [0, 'a', 8, 1, 'b', 9]

print(
    sum(
        zip(
            range(2), list('ab')
        ),
        (8, 9)
    )
)