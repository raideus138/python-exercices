'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla 
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista. '''
materias = input('Introduce tus materias separadas por una coma: ')
materias = materias.split(",")
for i in materias:
    print(f'Yo estudio {i.strip()}')