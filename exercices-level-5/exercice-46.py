'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''
tablas = [1,2,3,4,5,6,6,7,8,9,10]
for i in tablas:
    for n in tablas:
        print(f'{i} x {n} = {i*n}', end='\t')
    print()