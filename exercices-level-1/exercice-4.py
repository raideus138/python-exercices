'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def vocals(x):
    vocales = 'aeiou'
    if x in vocales:
        return True
    else:
        return False
print(vocals('x'))