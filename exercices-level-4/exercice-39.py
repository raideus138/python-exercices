'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''

vegetariana = ['Pimiento', 'Tofu']
no_vegetariana = ['Peperoni', 'Jamón', 'Salmón']

query = input('Que tipo de pizza quiere? (Vegetariana/No Vegetariana): ')
if query.lower() == 'vegetariana':
    print('Los ingredientes extra de su pizza pussy son:')
    for i in vegetariana:
        print(i)
elif query.lower() == 'no vegetariana':
    print('Los ingredientes de su pizza son:')
    for i in no_vegetariana:
        print(i)
else:
    print('lo escribiste mal aweonao')
extra = input('Eliga un ingrediente extra ademas de la mozzarela y los tomates que estan en todas las pizzas: ')

print(f'Su pizza es {query.capitalize()}, y su ingrediente extra es {extra}')