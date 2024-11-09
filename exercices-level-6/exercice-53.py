'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla. '''
materias = input('Introduce tus materias separadas por una coma: ')
materias = materias.split(",")
for i in materias:
    print(i.strip())