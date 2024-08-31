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
print(f'Tipo de dato: {type(my_other_set)}\n') # -> <class 'set'>

print(f'Cantidad de elementos en un set: {len(my_other_set)}\n') # -> 3

# (ADD) -> Agregando un elemento
my_other_set.add("MoureDev") # Un set no es una estructura ordenada
print(f'Elemento agregado en my_other_set: {my_other_set}')

my_other_set.add("MoureDev") # Un set no permite elementos duplicados, por lo que no se agrega de nuevo
print(f'Elemento duplicado no agregado en my_other_set: {my_other_set}\n') # -> {'Brais', 35, 'Moure', 'MoureDev'}

# (IN) -> Buscando un elemento en el set
print("Moure" in my_other_set) # -> True
print("Mouri" in my_other_set,'\n') # -> False

# (REMOVE) -> Eliminando un elemento
my_other_set.remove("Moure") # Si el elemento no existe, lanza un error KeyErro
print(f'Elemento eliminado en my_other_set: {my_other_set}\n') # -> {35, 'Brais', 'MoureDev'

# (CLEAR) -> Eliminando todos los elementos
my_other_set.clear()
print(f'Set vacio: {my_other_set}\n') # -> set()
print(f'Tipo de dato: {type(my_other_set)}\n') # -> <class 'set'>

# (DEL) -> Eliminando el set
del my_other_set
'''
print(f'Set eliminado: {my_other_set}') 
 -> NameError: name 'my_other_set' is not defined
'''

# Transformando de SET a LIST 
my_set = {"Brais", "Moure", 35}
my_list =  list(my_set)
print(f'Set transformado a List: {my_list}') # -> ['Brais', 35, 'Moure']
print(f'Tipo de dato: {type(my_list)}') # -> <class 'list'>
# Se accede a los elementos de la lista como en una lista normal
print(f'Accediendo a un indice: {my_list[0]}\n') # -> Brais

# Declaracion my_other_set nuevamente
my_other_set = {"Kotlin", "Swift", "Python"}

# (UNION) -> Uniendo dos sets
my_new_set = my_set.union(my_other_set)
print(f'Uniendo dos sets: {my_new_set}\n') # -> {'Brais', 'Swift', 'Python', 35, 'Moure', 'Kotlin'}
# Datos iguales no se agregan
print(f'Agregando elementos: {my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})}') # -> {'Brais', 'Swift', 'Python', 'JavaScript'}

# (DIFFERENCE) -> Diferencia entre dos sets
print(f'Diferencia entre dos sets: {my_new_set.difference(my_set)}') # -> {'Swift', 'Python', 'Kotlin' Arbitro, se resta el set de la izquierda menos el de la derecha
