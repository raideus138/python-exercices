
'''Escribir un programa que pida al usuario una palabra y muestre por pantalla
 el número de veces que contiene cada vocal.'''

palabra = str(input('Ingrese una palabra: '))
vocales = 'aeiou'
counter = 0
for char in palabra:
    for j in vocales:
        if char.lower() == j:
            counter += 1
print(counter)