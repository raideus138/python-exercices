'''Escribir una función que reciba una muestra de números en una lista y devuelva su media.'''
def media(*args):
    suma = 0
    for i in args:
        suma += i
    return suma/len(args)

print(media(1,2,3,4,5,6))