'''Escribir una función que reciba una muestra de números en 
una lista y devuelva un diccionario con su media, varianza y desviación típica.'''
import math


def estadisticas(lista):
    diccionario = {
        'media': sum(lista) / len(lista),
        'varianza': None,
        "desviacion tipica": None
    }
    varianza = 0
    for i in lista:
        varianza += (diccionario['media']-i)**2
    
    desviacion_tipica = math.sqrt(varianza)
    
    diccionario['varianza'] = varianza
    diccionario['desviacion tipica'] = desviacion_tipica
    
    return diccionario
    
print(estadisticas([1,2,3,4,5,6]))