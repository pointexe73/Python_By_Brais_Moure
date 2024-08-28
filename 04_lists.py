### LISTAS ###
'''
-my_list y my_other_list son dos listas vacías. 
-La primera se crea utilizando la función list()
-y la segunda utilizando corchetes [] (notación de lista).
'''
my_list =  list() # -> [] 
my_other_list = [] # -> []
 

# Imprimir la cantidad de elementos que tiene la lista.
print(f'Cantidad de elementos: {len(my_list)}') # -> 0
# Se imprime el tipo de elemento de (my_list) y (my_other_list)
print(f'Tipo de elemento de my_list = list(): {type(my_list)}') # -> <class 'list'>
print(f'Tipo de elemento de my_other_list = []: {type(my_other_list)}') # -> <class 'list'>
print()

# Se declara una lista
my_list = [35, 24, 62, 52, 30, 30, 17]
# Se imprime la lista 
print(f'Lista de elementos: {(my_list)}') # -> [35, 24, 62, 52, 30, 30, 17]
# Se imprime la cantidad de elementos que tiene la lista.
print(f'Cantidad de elementos: {len(my_list)}') # -> 7
print()

# Se declara una lista con elementos de diferentes tipos de datos (int, float, string).
my_other_list = [35, 1.77, "Brais", "Moure"]

# Se imprime el tipo de elemento 
print(f'Tipo de elemento: {type(my_other_list)}') # -> <class 'list'>

# Accediendo a elementos de la lista por su índice.
print(f'Mi edad es: {my_other_list[0]}') # -> 35
print(f'Mi estatura es: {my_other_list[1]}') # -> 1.77
print(f'Mi nombre es: {my_other_list[-1]}') # -> "Moure"
print(f'Mi apellido es: {my_other_list[-4]}') # -> 35
print(f'Devuelve la cantidad de elementos parecidos: {my_other_list.count("Brais")}') # -> 1
print()
'''
-Se intenta acceder a un índice que no existe en la lista, 
lo cual genera un error de índice fuera de rango (IndexError).
'''

age, height, name, surname = my_other_list # -> Desempaquetado de la lista
# Se imprime los elementos de la lista
print(f'Mi nombre es {name}. Mi apellido es {surname}. Mi estatura es {height}. Mi edad {age}') # -> Brais Moure 1.77 35
print()

# Concatenar dos listas
print(f'Concatenar dos listas: {my_list + my_other_list}') # -> [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']
print()

# (APPEND) -> Agregando un elemento a la lista (my_other_list)
my_other_list.append("MoureDev") # El elemento se agrega al final de la lista
print(f'Se agrego un elemento con APPEND: {my_other_list}') # -> [25, 1.77, 'Brais', 'Moure', MoureDev] 

# (INSERT) -> Inserta un elemento en un lugar específico de la lista (my_other_list)
my_other_list.insert(1, "Rojo") # El elemento se inserta en el índice 1 de la lista
print(f'Se inserto un elemento con INSERT: {my_other_list}') # -> [25, Rojo, 1.77, 'Brais', 'Moure', MoureDev]

# (REMOVE) -> Remueve un elemento de la Lista
my_other_list.remove("Rojo") 
print(f'Se removio un elemento con REMOVE: {my_other_list}') # -> [25, 1.77, 'Brais', 'Moure', MoureDev]
my_list.remove(30) # -> Remueve el primer elemento que encuentra con el valor 30
print(f'Se removio un elemento con REMOVE: {my_list}') # -> [35, 24, 62, 52, 30, 17]

# (POP) -> Remueve el último elemento de la lista y lo devuelve como resultado.
print(f'Se removio un elemento con POP: {my_list.pop()}') # Se elemino el ultimo elemento -> 17
print(f'Remover un elemento con POP: {my_list}') # -> [35, 24, 62, 52, 30]
  
# Guardo el elemento eleminado de (my_list) en una variable -> my_pop_element
my_pop_element = my_list.pop(2) # Elemento que se elimino en la pocicion 2
print(f'Elemento eliminado: {my_pop_element}') # -> 62  
print(f'Lista con elementos eliminados: {my_list}') # -> [35, 24, 52, 30]

# (DEL) -> Elimina un elemento de la lista por su índice. No devuelve el elemento eliminado como resultado.
del my_list[2] # -> Elimina el elemento en la posicion 2
print(f'Se elemino el elemento con DEL: {my_list}') # -> [35, 24, 30]

# (COPY) -> Crea una copia superficial de la lista original. Los cambios en la copia no afectan a la lista original
my_new_list = my_list.copy() # -> Crea una copia de la lista (my_list) en la variable (my_new_list)

# (CLEAR) -> Elimina todos los elementos de la lista. No devuelve ningún resultado, simplemente vacía la lista.
my_list.clear() # -> Elimina todos los elementos de la lista
print(f'Se elemino todos los elementos con CLEAR: {my_list}') # -> []

# Imprime la copia creada con COPY
print(my_new_list) # -> [35, 24, 30]

# (REVERSE) -> Invierte el orden de los elementos en la lista.
my_new_list.reverse() # -> Invierte el orden de los elementos en la lista
print(f'Se invirtio el orden de los elementos con REVERSE: {my_new_list}') # -> [30, 24, 35]

# (SORT) -> Ordena los elementos de la lista en orden ascendente
my_new_list.sort() # -> Ordena los elementos de la lista en orden ascendente
print(my_new_list) # -> [24, 30, 35]
print()

# Reemplando el valor de (my_list) de Lista a Variable de tipo String
my_list = "Hola Python"
print(my_list) # -> Hola Python
print(type(my_list)) # -> <class 'str'>
