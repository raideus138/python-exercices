
'''Escribir una función que simule una calculadora científica que permita calcular el seno,
 coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor 
 y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
 y el resultado de aplicar la función a esos enteros. '''
from math import sin, cos, tan, exp, log

def apply_function(f, n):

    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()
