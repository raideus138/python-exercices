'''Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.'''
nombre = input('Ingrese su nombre: ')
for i in range(1,11):
    print(f'{i} {nombre}')