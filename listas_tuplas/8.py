word = input("Escribe una palabra: ")
word = word.replace(" ", "")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
print(word)
print(reversed_word)

if word == reversed_word:
    print("Es palindromo")
else:
    print("No es palindromo")
