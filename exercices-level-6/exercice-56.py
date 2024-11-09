'''Escribir un programa que pregunte al usuario los números ganadores de 
la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''
numeros_ganadores = input('Ingrese los numeros ganadores de la loteria: ')
numeros_ganadores = numeros_ganadores.split(',')
numeros_ganadores.sort()
print(numeros_ganadores)