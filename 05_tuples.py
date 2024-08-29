### TUPLAS ###

''' my_tuple y my_other_tuple son tuplas. 
    Las tuplas son listas inmutables, es decir, no se pueden modificar
    una vez creadas. Para crear una tupla, se utilizan paréntesis () en lugar de corchetes []
'''

my_tuple = tuple() # -> Tupla vacía
my_other_tuple = () # -> Tupla vacía

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
print(f'Contenido de la tupla: {my_tuple}') # -> 35 1.77 Brais Moure
print(f'Tipo de dato: {type(my_tuple)}\n') # -> <class 'tuple'>


print(f'Imprime el valor 0: {my_tuple[0]}') # -> 35
print(f'Imprime el valor -1: {my_tuple[-1]}\n') # -> Moure
'''
print(my_tuple[4]) IndexError: tuple index out of range
print(my_tuple[-6]) # -> IndexError: tuple index out of range
'''

# (COUNT) -> Cuenta el número de veces que aparece un elemento en la tupla
print(f'Numero de veces que aparace "Brais": {my_tuple.count("Brais")}') # -> 1

# (INDEX) -> Devuelve el índice de la primera aparición de un elemento en la tupla
print(f'Devuelve el indice del valor "Moure": {my_tuple.index("Moure")}') # -> 3
print(f'Devuelve el indice del valor "Brais": {my_tuple.index("Brais")}\n') # -> 2 

'''
Las tupla son inmutables, por lo que no se pueden modificar
my_tuple[1] = 1.80  
print(my_tuple) -> TypeError: 'tuple' object does not support item assignment
'''

# Sumar dos tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(f'Suma de tuplas: {my_sum_tuple}\n') # -> (35, 1.77, 'Brais', 'Moure', 'Brais', 35, 60, 30)

# Imprime moure y Brais y 35
print(f'Subtuplas: {my_sum_tuple[3:6]}\n') # -> ('Moure', 'Brais', 35)

# Pasar una tupla a lista
my_tuple = list(my_tuple)
print(f'Tupla convertida a lista: {my_tuple}') # -> [35, 1.77, 'Brais', 'Moure', 'Brais']
print(f'Tipo de dato: {type(my_tuple)}\n') # -> <class 'list'>


# my_tuple es una lista, por lo que se puede modificar
my_tuple[4] = "Mouredev" # -> Modificar un valor de la lista
my_tuple.insert(1, "Azul") # -> Insertar un valor en la lista

# Pasar una lista a tupla
my_tuple = tuple(my_tuple)
print(f'Lista convertida a tupla: {my_tuple}') # -> (35, 'Azul', 1.77, 'Brais', 'Mouredev')
print(f'Tipo de dato: {type(my_tuple)}\n') # -> <class 'tuple'>

'''
del my_tuple
print(my_tuple) # -> NameError: name 'my_tuple' is not defined
'''