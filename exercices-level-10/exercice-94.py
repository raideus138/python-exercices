'''Escribir una función que pida un número entero entre 1 y 10 y 
guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
done n es el número introducido.'''
def number(n):
    file = open(f'tabla-{n}.txt', 'w')
    for i in range(1,11):
        file.write(f'{i} x {n} = {i*n}\n')

number(5)