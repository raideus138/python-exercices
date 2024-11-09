'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''

inputs = input('Ingrese dos numeros enteros: ')
numeros = inputs.split(" ")
num1 = int(numeros[0])
num2 = int(numeros[1])
cociente = num1 // num2
resto = num1 % num2
print(f'El resto de la division de los numeros es {resto} y el cociente es {cociente}')