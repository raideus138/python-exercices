'''
Las matemáticas financieras, resumidas en una frase, las podríamos definir como la rama 
de las matemáticas que estudia los flujos de dinero a través del tiempo. 
Básicamente se presupone que el dinero tiene menos valor en el futuro que en el presente, 
ya sea por un tema inflacionario o por la preferencia natural de las personas a priorizar el consumo presente.

El valor futuro es el valor alcanzado por un determinado capital al final del período determinado 
(para el ejemplo usaremos la fórmula del interés compuesto). 
Para calcularlo se utiliza la siguiente fórmula

    VF = VA * (1+i)^n

El valor presente de una inversión es cuando calculamos el valor actual que tendrá una determinada cantidad
que recibiremos o pagaremos en un futuro. Para calcularlo se utiliza la siguiente fórmula

    VA = (VF)/(1 + i)^n

Donde 
    VF es el valor futuro, 
    VA es el valor actual o inicial de la inversión, 
    i es  el tipo de interés y 
    n es número de años de la inversión.

Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el 
valor futuro de la inversión cada año del periodo indicado.

Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el 
valor actual del capital cada año del periodo indicado.
'''

def vf(capital, tipo, periodo):
    for i in range(periodo):
        print("Año", i, ":", capital * (1 + tipo / 100) ** (i + 1))
    return

def va(capital, tipo, periodo):
    for i in range(periodo): 
        print("Año", -i, ":", capital / (1 + tipo / 100) ** (i + 1))
    return

cantidad = float(input("Introduce un capital: "))
tipo = float(input("Introduce un tipo de interés: "))
años = int(input("Introduce un número de años: "))

print("VALOR FUTURO")
vf(cantidad, tipo, años)
print("VALOR ACTUAL")
va(cantidad, tipo, años)