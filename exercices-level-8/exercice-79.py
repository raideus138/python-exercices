'''Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.'''
def cuadrados(*x):
    return [i**2 for i in x]
print(cuadrados(1,2,3,4,5,6,))