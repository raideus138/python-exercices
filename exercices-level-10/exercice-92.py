import math

'''Escribir una función que calcule el módulo de un vector. '''
def modulo(vector):
    x =  vector[0]**2
    y =  vector[1]**2
    x_y = x + y
    return math.sqrt(x_y)

print(modulo([4,5]))