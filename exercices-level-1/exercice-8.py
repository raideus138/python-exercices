'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''
def superposicion(a,b):
    status = False
    for i in a:
        if a[i-1] == b[i-1]:
            status = True
    return status

print(superposicion([1,2,3,4,5],[9,8,7,6,5]))