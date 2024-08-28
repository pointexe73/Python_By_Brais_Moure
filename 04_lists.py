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