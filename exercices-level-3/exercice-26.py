'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula'''

frase = input('ingrese una frase: ')
vocal = input('ingrese una vocal: ')

frase = frase.replace(vocal, vocal.upper())
print(frase)