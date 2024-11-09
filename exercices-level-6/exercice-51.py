'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.'''

frase = input('Ingrese una frase y una letra (separados por una coma): ')
frase = frase.split(',')

if len(frase) != 2:
    print("Por favor, ingrese una frase y una letra, separados por una coma.")
else:
    texto = frase[0].strip()
    letra = frase[1].strip() 
    veces = 0

    for char in texto:
        if char.lower() == letra.lower():
            veces += 1

    print(f'La letra "{letra}" se repite {veces} veces.')

