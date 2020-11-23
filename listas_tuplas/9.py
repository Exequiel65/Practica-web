word = input("Escribe una frase: ")
vocals = ["a", "e", "i", "o", "u"]

for vocal in vocals:
    count = 0
    for letter in word:
        if letter == vocal:
            count += 1
    print("La letra " + vocal + " se repite " + str(count))