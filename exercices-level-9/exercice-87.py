'''Escribir una función que reciba otra función booleana y una lista, 
y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.'''
def filtra_lista(funcion, lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(filtra_lista(par, [1, 2, 3, 4, 5, 6]))