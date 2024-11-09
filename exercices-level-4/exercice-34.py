'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error. '''
numeros = input('Ingrese dos numeros separados por una coma: ')
n1 = numeros.split(",")[0]
n2 = numeros.split(",")[1]
if n2 == 0:
    print('No se puede dividir entre 0')
else:
    print(n1 / n2)
    