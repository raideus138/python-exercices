'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''
def sum(arreglo):
    total = 0
    for i in arreglo:
        total += i
    return total
def multip(arreglo):
    total = arreglo[0]
    for i in arreglo:
        total *= i
    return total

print(sum([1,2,3,4,]))
print(multip([1,2,3,4]))