# dates = ["Nombre", "Apellido", "Edad", "Sexo", "Télefono", "Correo electronico"]
# personal_information = {}
# for date in dates:
#     new = input("Escriba su " + date + ": ")
#     personal_information[date] = new
#     print("El " + date + " ingresado es: " + new.capitalize())

# print(personal_information)

person = {}
more = "Si"
while more == "Si":
    key = input("Que dato quiere ingresar? ")
    value = input(": ")
    person[key] = value
    print(person)
    more1 = input("Quieres añadir mas información (Si/No)")
    more = more.capitalize()