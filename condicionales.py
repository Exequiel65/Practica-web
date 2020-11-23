# 1
# edad = int(input("Que edad tienes?: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")


# 2
# password = "age23nfsu2"

# user_password = input("Ingrese su contraseña: ")

# if password == user_password.lower():
#     print("Contraseña es correcta.")
# else:
#     print("Contraseña incorrecta.")

# 3

# number1 = int(input("Ingrese un número: "))
# number2 = int(input("Igrese un segundo número: "))

# if number2 == 0:
#     print("No es posible dividir por 0")
#     number2 = int(input("Escriba nuevamente el número: "))
#     division = number1 / number2
#     print("El resultado es: " + str(division))
# else:
#     division = number1 / number2
#     print("El resultado es: " + str(division))

# 4

# number = int(input("Escriba un número: "))

# if number % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# 5
# edad = int(input("Escriba su edad: "))
# ingresos = int(input("Escriba su ingreso mensual: "))

# if edad < 18:
#     print("Es menor de edad, no debe tributar")
# elif ingresos < 1000:
#     print("Sus ingresos en menor del establecido, no puede tributar")
# else:
#     print("Debe tributar")

# 6

# name = input("Cual es tu nombre?: ")
# gender = input("Elije tu sexo, (M , F): ")

# if gender.lower() == "m":
#     if name.lower() > "n":
#         print("Grupo A")
#     else:
#         print("Grupo B")
# elif gender.lower() == "f":
#     if name.lower() < "m":
#         print("Grupo A")
#     else:
#         print("Grupo B")

# 7

# renta_anual = int(input("Ingrese su el monto de su renta anual: "))

# if renta_anual < 10000:
#     print("Su tipo impositivo es del 5%.")
# elif renta_anual > 10000 and renta_anual < 20000:
#     print("Su tipo impositivo es del 15%.")
# elif renta_anual > 20000 and renta_anual < 35000:
#     print("Su tipo impositivo es del 20%.")
# elif renta_anual > 35000 and renta_anual < 60000:
#     print("Su tipo impositivo es del 30%.")
# else:
#     print("Su tipo impositivo es del 45%.")

# 8

# puntuacion = float(input("Ingrese su puntuación: "))

# if puntuacion == 0.0:
#     ren = "inaceptable"
#     nivel = 0
# elif puntuacion == 0.4:
#     ren = "Aceptable"
#     nivel = 0.4
# elif puntuacion >= 0.6:
#     ren = "Meritorio"
#     nivel = 0.6

# else:
#     nivel = ""


# if nivel == "":
#     print("Esta puntuación no es valida.")
# else:   
#     print("Su nivel de rendimiento es " + ren , "\n","Te corresponde cobrar " + str(2400 * nivel) + " euros")

# 9

# age = int(input("Edad de la persona: "))

# if age <= 4:
#     tex = "gratis"
# elif age < 18:
#     tex = 5
# else:
#     tex = 10

# if tex == "gratis":
#     print("Entra gratis")
# else:
#     print("Debe abonar " + str(tex) + " euros")

# 10

print(""" 
      B I E N V E N I D @
            
             A

    PIZZERIA BELLA NAPOLI

Tipos de pizza
    1- Vegetariana
    2- No vegetariana

""")

tipo = int(input("Intreduce el número del tipo de pizza a elejir: "))

if tipo == 1:
    print("Ingredientes de pizzas vegetarianas \n 1- Pimiento \n 2- Tofu \n")
    ingrediente = input("Introduzca el número del ingrediente que desea: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
elif tipo == 2:
    print("Ingredientes de pizzas no vegetarianas \n 1- Peperoni \n 2- Jamón \n 3- Salmón \n")
    ingrediente = input("Introduzca el número del ingrediente que desea: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    elif ingrediente == "3":
        print("salmón")
    else:
        print("Elija una opción correcta")       
else:
    print("Número incorrecto, porfavor elija una opcion correcta.")
    

