### SETS ###

''' 
my_set y my_other_set son dos variables que se utilizan-
para almacenar colecciones de elementos únicos
'''

my_set = set() # -> Set vacio
my_other_set = {} # -> Set vacio

print(f'Tipo de dato: {type(my_set)}') # -> <class 'set'>
# Si el set esta vacio, se imprime como un diccionario 
print(f'Tipo de dato: {type(my_other_set)}') # -> <class 'dict'>

 
my_other_set = {"Brais", "Moure", 35} 
# Si el set tiene elementos, se imprime como un set
print(f'Tipo de dato: {type(my_other_set)}') # -> <class 'set'>