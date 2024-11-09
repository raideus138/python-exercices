'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. '''
data = input('ingrese su edad y sus ingresos separados por una coma: ')
edad = int(data.split(',')[0])
ingresos = int(data.split(',')[1])
if edad >= 16 and ingresos >= 1000:
    print('debes tributar tus impuestos')
else:
    print('no debes tributar tus impuestos')