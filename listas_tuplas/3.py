subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
note = []
for subject in subjects:
    notes= input("Que nota has sacado en " + subject + ": ")
    note.append(notes)
for i in range(len(subject)):
    print("Tu nota en " + subjects[i] + "es: " + note[i])


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])