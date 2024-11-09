'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 la cuenta atrás desde ese número hasta cero separados por comas.'''

numero = int(input('Ingrese un numero positivo: '))

print
for i in range(numero+1):
    print(numero - i)