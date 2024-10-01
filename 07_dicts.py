### DICTIONARY ###

my_dict = dict()
my_other_dict = {}


print(f'Tipo de dato: {type(my_dict)}') # -> <class 'dict'>
print(f'Tipo de dato: {type(my_other_dict)}') # -> <class 'dict'>

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}


my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
    } # Lenguajes tiene como valor un SETS

print(my_other_dict) # -> {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}</pre>
print(my_dict) # -> {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Swift', 'Kotlin'}}, 1: 1.77

# Imprime la cantidad de ítems que tiene el diccionario
print(f'Cantidad de items: {len(my_other_dict)}') # -> Cantidad de items: 4
print(f'Cantidad de items: {len(my_dict)}') # -> Cantidad de items: 5

5.20.57