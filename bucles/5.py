inversion = float(input("Ingrese un monto: "))
interest = int(input("Interes anual: "))
years = int(input("Cantidad de años: "))

for i in range(years):
    inversion *= 1 + interest / 100
    print("Capital tras " + str(i + 1) + " años: " + str(round(inversion, 2)))

