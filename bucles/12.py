setence = input("Escribe una frase: ")
letter = input("Escribe una letra: ")

counter = 0

for i in setence:
    if i == letter:
        counter += 1

print("La letra " + letter + " aparece " + str(counter) + " veces en la frase " + setence)
