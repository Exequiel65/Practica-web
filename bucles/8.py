number = int((input("Escriba un número entero: ")))

for i in range(1, number + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
   