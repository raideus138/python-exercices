'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca
 hasta que el usuario escriba “salir” que terminará.'''

while True:
    n = input('Introduce algo: ')
    if n.lower() != 'salir':
        print('Cuek')
    else:
        break