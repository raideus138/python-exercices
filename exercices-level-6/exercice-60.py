'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''
palabra = str(input('Ingrese una palabra: '))
if palabra[::-1] != palabra:
    print('La palabra ingresada no es un palíndromo')
else:
    print('La palabra ingresada es un palíndromo')