### STRINGS ###


my_string = "Mi String"
my_other_string = 'Mi otro String'

# Imprime la longitud de la cadena de texto
print(len(my_string)) # -> 9
print(len(my_other_string)) # -> 12

# Concatenación de cadenas de texto
print(my_string + " " + my_other_string) # -> Mi String Mi otro String

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string) # -> Este es un String con salto de linea

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string) # -> Este es un String con tabulación

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string) # -> \tEste es un String \n escapado


## Formateo ##

name, surname, age = "Brais", "Moure", 35

# Imprime utilizando Format
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # -> Mi nombre es Brais Moure y mi edad es 35
# Imprime utilizando %s para cadenas de texto y %d para números
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # -> Mi nombre es Brais Moure y mi edad es 35
# Imprime utilizando f-strings
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # -> Mi nombre es Brais Moure y mi edad es 35

## Desempaquetado de caracteres ##

language = "python"
a, b, c, d, e, f = language # -> p y t h o n
print(a) # -> p
print(e) # -> o

## Divicion ## 2.48.05