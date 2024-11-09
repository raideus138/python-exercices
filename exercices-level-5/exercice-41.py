'''Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
año_actual = 2024
edad = int(input("Ingrese su edad: "))
for i in range(1, edad+1):
    print(año_actual - i)