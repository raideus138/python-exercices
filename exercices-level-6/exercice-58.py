'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista
 las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas
  que el usuario tiene que repetir.'''
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?: ")
    scores.append(score)
repetir = []
for subject in subjects:
    if scores[subjects.index(subject)] >= 5:
        repetir.append[subject]
print(f'Tienes que repetir {repetir}')