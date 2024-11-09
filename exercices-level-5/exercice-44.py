'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''
cantidad = float(input('Ingrese la cantidad a invertir: '))
interes = float(input('Ingrese el interes anual: '))
años = int(input('Ingrese el número de años: '))

for i in range(1, años+1):
    cantidad = (cantidad * interes) + cantidad
    print(f'El capital obtenido en el año {i} es: {round(cantidad, 2)}$')