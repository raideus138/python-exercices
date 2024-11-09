'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def len(str):
    len = 0
    str = str.replace(" ", "")
    for char in str:
        len += 1
    return len

print(len('hola che'))