# a = 3
# b = 2
# c = 5

# suma = a + b
# multiply = b * c

# divid = suma / multiply

# exp = divid ** b

# print(exp)

# print(((3 + 2) / (2 * 5)) ** 2)


# time_job = int(input("Cuantas horas trabajas?: "))
# cost_time = int(input("Cuanto te pagan la hora de trabajo?: "))

# job_daily_cash = time_job * cost_time
# mess_job = job_daily_cash * 22

# print("Tu pago por dia es de " + str(job_daily_cash) + "\n")

# print("Y al mes tu sueldo es: $ " + str(mess_job))




# 8
# n = int(input("Ingrese un numero entero desde el 1 a 100: "))
# suma = ((n * (n + 1)) / 2)
# print(str(suma))

# 9
# peso = float(input("Cual es su peso?: "))
# altura = float(input("Cual es su estatura?: "))

# imc = peso / (altura ** 2)
# imc = round(imc, 2)
# print("Su imc es " + str(imc))


# 10
# n = input("Ingrese un numero: ")
# m = input("Ingrese otro numero: ")

# cociente = int(n) // int(m)
# resto = int(n) % int(m)
# print("{} entre {} da un conciente {} y un resto {}.".format(n, m, cociente, resto))

#11


# if __name__ == "__main__":
#     print("""
#         B I E N V E N I D O  A 
#         INVERSIONES M.A. S.A. """)
#     interes_Anual = 10
#     mon_invert = int(input("Ingrese un monto en Pesos argentinos a invertir: "))
#     tiempo = int(input("Ingrese la cantidad de años: "))
    

#     ganancia_anual = (mon_invert * interes_Anual) / 100
#     ganancia_total = ganancia_anual * tiempo

#     print("La ganancia con el monto de ${} por la cantidad de {} años, es de ${} por año y de ${} por la cantidad de año que elijio".format(mon_invert, tiempo, ganancia_anual, ganancia_total))

#12

# payaso = 112
# muñeca = 75
# payaso_vend = int(input("Cantidad de payasos vendidos: "))
# muñeca_vend = int(input("Cantidad de muñecas vendidas: "))

# peso_paq = (payaso * payaso_vend) + (muñeca * muñeca_vend)

# print("El peso total para el envio es", str(peso_paq),"gramos")

# 13
# interes = 1.04

# dinero_depositado = float(input("Ingrese un monto a depositar: "))
# balance = dinero_depositado * interes
# print("Balance tras el primer año: " + str(round(balance, 2)))
# balance2 = balance * interes
# print("Balance tras el segundo año: {}".format(round(balance2, 2)))
# balance3 = balance2 * interes
# print("Balance tras el tercer año: {}".format(round(balance3, 2)))

# 14

# barra_pan = 3.49
# pan_ayer = (barra_pan * 40) / 100

# barra_pan_ayer_vend = int(input("Ingrese la cantidad de pan de dia anterior a vender: "))
# precio_total = pan_ayer * barra_pan_ayer_vend
# precio_total = round(precio_total, 2)

# print("El precio total es: " + str(precio_total) + " euros")