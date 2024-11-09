'''Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
 resultado de aplicar la función dada a cada uno de los elementos de la lista. '''
def aplica_funcion_lista(funcion, lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))