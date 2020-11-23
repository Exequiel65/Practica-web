# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# scores = []
# aproved = []
# for subject in subjects:
#     score = int(input("Escribe la nota de " + subject + ": "))
#     scores.append(score)
#     if score >= 6:
#         aproved.append(subject)
# for subject in aproved:
#     subjects.remove(subject)
# print("Debes rendir " + str(subjects))


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
aproved = []

for i in range(len(subjects)- 1, -1, -1):
    score = int(input("Escriba la nota de " + subjects[i] + ": " ))
    if score >= 6:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))

