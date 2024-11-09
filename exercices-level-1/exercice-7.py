'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''
def palindromo(str):
    if str == str[::-1]:
        return True
    else:
        return False
print(palindromo('hola che'))