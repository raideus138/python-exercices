'''
Dadas dos listas de números del mismo tamaño x e y, construir las siguientes funciones:

1. Una función para calcular la media de una lista de números.
2. Una función para calcular la varianza de una lista de números.
3. Una función para calcular la covarianza de dos listas de números.
5. Una función para calcular los coeficientes de la recta de regresión de y sobre x.
6. Una función que devuelva el diagrama de dispersión y la recta de regresión como la que se muestra en el siguiente ejemplo:
'''

x = [3,2,5,7]
y = [5,6,3,8]

def media(lista):
    return lista/len(lista)

def varianza(lista):
    m  = media(lista)
    xi = 0
    for i in lista:
        xi += (xi - m)**2
    varianza =  xi/(len(lista)-1)
    return varianza

def covarianza(x,y):
    mx = media(x)
    my = media(y)
    total = 0
    for i in range(1,x+1):
        total += (x[i-1]-mx)*(y[i-1]-my)
    return (total)/len(x)

def coeficientes(x, y):
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    numerador = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    denominador = sum((x[i] - mx) ** 2 for i in range(n))
    b = numerador / denominador
    a = my - b * mx
    return a, b

