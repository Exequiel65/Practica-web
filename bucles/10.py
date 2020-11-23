number = int(input("Escribe un número: "))
i = 2
while number % i != 0:
   i += 1
if i == number:
    print(str(number) + " es primo")
else:
    print("no es primo")
