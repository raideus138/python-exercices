'''Escribir una función que pida dos números n y m entre 1 y 10, 
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje 
por pantalla informando de ello.'''
def numbers(n,m):
    nombre_fichero = 'tabla-'+str(n)+'.txt'
    try:
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
            print(f'El contenido de la linea {m} es: {lineas[m-1]}')
    except FileNotFoundError:
        print('El fichero no existe')
numbers(5,3)