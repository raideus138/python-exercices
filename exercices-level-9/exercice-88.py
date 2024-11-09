'''Escribir una función que reciba una frase y devuelva un diccionario 
con las palabras que contiene y su longitud. '''
def contador(frase):
    words = frase.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(contador('pene ultra duro'))