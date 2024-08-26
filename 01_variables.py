### VARIABLES ###

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable =  False
print(my_bool_variable)

# Concatenacion de variaables en un print
print(my_int_variable,  my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Una funcion del sistema
print(len(my_string_variable))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Juan", "Diaz", "Juandc", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs

name = input('What is your name: ')
age = input('How old are you? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Juan"
print(name)
print(age)


# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
address = True
address = 5
address = 1.2
print(type(address))