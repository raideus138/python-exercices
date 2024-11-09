import math

'''Escribir una función que calcule el área de un círculo y otra que calcule 
el volumen de un cilindro usando la primera función.
'''
def circulo(a, radio = 0, altura = 0):
    if a == 'volumen':
        return math.pi*math.pow(radio, 2)*altura
    elif a == 'area':
        return math.pi*math.pow(radio, 2)
