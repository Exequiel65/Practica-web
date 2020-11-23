number = []

for i in range(10):
    new_number = int(input("Escribe el numero ganador: "))
    number.append(new_number)
        
number.sort()

print("Los numeros ganadores son : " + str(number))