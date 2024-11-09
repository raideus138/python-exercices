'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%. '''
def calc_iva(precio, porc=0.021):
    return (int(precio) * porc) + precio

print(calc_iva(500))