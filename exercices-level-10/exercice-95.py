'''Escribir una función que pida un número entero entre 1 y 10, 
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido,
 y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''

n = int(input('Introduce un numero de el 1 al 10: '))
nombre_fichero = 'tabla-'+str(n)+'.txt'
try:
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print('El archivo no existe')
else:
    print(f.read())
    f.close()
