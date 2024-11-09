'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
las letras de la palabra introducida empezando por la última.
        '''
palabra = input('Ingrese una palabra: ')
palabra = palabra[::-1]
for char in palabra:
        print(char)