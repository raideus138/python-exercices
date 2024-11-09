'''Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''
import math as m
muestra_numeros = input('Inghrese una muestra de numeros separados por comas: ')
muestra_numeros = muestra_numeros.split(',')

suma_numeros = 0
for i in muestra_numeros:
    suma_numeros += int(i)
media = suma_numeros/len(muestra_numeros)

numerador = 0

for i in muestra_numeros:
    a = pow(int(i)-media,2)
    numerador += a

desviacion = m.sqrt(numerador/len(muestra_numeros))
print(f'La media es: {media}. la desviacion tipica es {desviacion}')