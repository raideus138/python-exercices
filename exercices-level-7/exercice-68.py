'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de 
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por 
pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.'''
creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos_totales = 0
for i in creditos:
    creditos_totales += creditos[i]
    print(f'{i} tiene {creditos[i]} créditos')
print(f'Los creditos totales son {creditos_totales}')