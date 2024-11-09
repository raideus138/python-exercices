'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
fecha = input('Ingrese una fecha en formato (dd/mm/aaaa): ')
fecha = fecha.split('/')
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
print(f'{fecha[0]} de {meses[int(fecha[1])-1]} de {fecha[2]}')