'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''

def histograma(arreglo):
    for i in arreglo:
        print(i * '*')
histograma([5,3,65])