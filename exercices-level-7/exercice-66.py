'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y
 lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
  vive en <dirección> y su número de teléfono es <teléfono>.'''
data = input('Ingrese su nombre, edad, dirección y teléfono. Separados por comas: ')
data = data.split(',')

diccionario = {
    'nombre': data[0],
    'edad': data[1],
    'direccion': data[2],
    'telefono': data[3]
}
print(f'{diccionario["nombre"]} tiene {diccionario["edad"]} años, vive en {diccionario['direccion']} y su numero de telefono es {diccionario["telefono"]}')