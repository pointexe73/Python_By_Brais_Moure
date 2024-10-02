### DICTIONARY ###

my_dict = dict()
my_other_dict = {}


print(f'Tipo de dato: {type(my_dict)}') # -> <class 'dict'>
print(f'Tipo de dato: {type(my_other_dict)}\n') # -> <class 'dict'>

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}


my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
    } # Lenguajes tiene como valor un SETS

print(f'Mi my_other_dict es: {my_other_dict}') # -> Mi my_other_dict es: {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}</pre>
print(f'Mi my_dict es: {my_dict}\n') # -> Mi my_dict es: {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Swift', 'Kotlin'}}, 1: 1.77

# Imprime la cantidad de ítems que tiene el diccionario
print(f'Cantidad de items: {len(my_other_dict)}') # -> Cantidad de items: 4
print(f'Cantidad de items: {len(my_dict)}\n') # -> Cantidad de items: 5

print(f'Valor de Nombre es: {my_dict["Nombre"]}') # -> Valor de Nombre es: Brais

# Cambiar el valor de ítem Nombre 
my_dict["Nombre"] = "Pedro"
print(f'Valor de Nombre es: {my_dict["Nombre"]}\n') # -> Valor de Nombre es: Pedro

# Añadir un nuevo ítem al diccionario
my_dict["Calle"] = "Calle Moure"
print(f'Mi my_dict es: {my_dict}\n') # -> Mi my_dict es: {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Swift', 'Kotlin'}, 1: 1.77, 'Calle': 'Calle Moure'}

# Eliminar un ítem del diccionario
del my_dict["Calle"]
print(f'Mi my_dict es: {my_dict}\n') # -> Mi my_dict es: {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Swift', 'Kotlin'}, 1: 1.77}

print(f'Esta en el diccionario: {"Moure" in my_dict}') # -> Esta en el diccionario: False, porque busca la clave, no el valor
print(f'Esta en el diccionaruo: {"Apellido" in my_dict}\n') # -> Esta en el diccionaruo: True, porque busca la clave, no el valor

# Imprimir el valor de my_dict["Apellido"]
print(f'Valor de Apellido es: {my_dict["Apellido"]}\n') # -> Valor de Apellido es: Moure

