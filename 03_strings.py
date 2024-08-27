### STRINGS ###


my_string = "Mi String"
my_other_string = 'Mi otro String'

# Imprime la longitud de la cadena de texto
print(f'Longitud de la cadena: {len(my_string)}\n') # -> 9
print(f'Longitud de la cadena: {len(my_other_string)}\n') # -> 12

# Concatenación de cadenas de texto
print(f'Concatena dos cadenas: {my_string + " " + my_other_string}\n') # -> Mi String Mi otro String

my_new_line_string = "Este es un String\ncon salto de linea"
print(f'Salto de linea con \\n: {my_new_line_string}\n') # -> Este es un String con salto de linea

my_tab_string = "\tEste es un String con tabulacion"
# Doble \\ para que se imprima el caracter \
print(f'Tabulacion con \\t: {my_tab_string}\n') # -> Este es un String con tabulación

my_scape_string = "\\tEste es un String \\n escapado"
print(f'Doble \\ para ver \\n y \\t: {my_scape_string}\n') # -> \tEste es un String \n escapado


## Formateo ##
print("FORMATEO\n")
name, surname, age = "Brais", "Moure", 35

# Imprime utilizando Format
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # -> Mi nombre es Brais Moure y mi edad es 35
# Imprime utilizando %s para cadenas de texto y %d para números
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # -> Mi nombre es Brais Moure y mi edad es 35
# Imprime utilizando f-strings
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # -> Mi nombre es Brais Moure y mi edad es 35
print()

## Desempaquetado de caracteres ##
print("DESEMPAQUETADO DE CARACTERES\n")

language = "python"
a, b, c, d, e, f = language # -> p y t h o n
print(f'a = p -> {a}') # -> p
print(f'e = o -> {e}') # -> o
print()

## Divicion ## 
print("DIVICION DE CADENAS\n")

language_slice = language[1:3] # -> yt
print(f'Divicion de cadena[1:3]: {language_slice}\n') # -> yt

language_slice = language[1:] # -> ython
print(f'Divicion de candena[1:]: {language_slice}\n') # -> ython

language_slice = language[-2] # -> o
print(f'Divicion de cadena[-2]: {language_slice}\n') # -> o

# 0:6:2 -> Empieza en el 0, termina en el 6 y salta de 2 en 2
lenguaje_slice = language[0:6:2] # -> pto
print(f'Divicion de cadena[0:6:2]: {lenguaje_slice}\n') # -> pto

## Reverse strings ##
print("REVERSE STRINGS")

# ::-1 -> Empieza desde el final y va hacia atrás
reversed_language = language[::-1] # -> nohtyp
print(f'Reverso de cadena[::-1]: {reversed_language}\n') # -> nohtyp


## Funciones del sistema ##
print("FUNCIONES DEL SISTEMA\n")

# Imprime la primera letra en mayusculas
print(f'Primera letra Mayucula: {language.capitalize()}') # -> Python

# Imprime todas las letras en mayusculas
print(f'Todas las letras en Mayusculas: {language.upper()}') # -> PYTHON

# Encuentra la cantidad de letra (t) que hay en la cadena de texto
print(f'Cuantas letras hay: {language.count("t")}') # -> 1

# Verifica si la cadena de texto contiene numero --> False o True
print(f'Contiene numero: {language.isnumeric()}') # -> False

# 1 es un numero --> True o False
print(f'Contiene numero: {"1".isnumeric()}') # -> True

# Imprime todas las letras en minusculas
print(f'Todas las letras en minusculas: {language.lower()}') # -> python

# .UPPER Pasa a mayuśculas, isupper Pasa True si estan en mayusculas y no False
print(f'Comprueba si todas con Mayuculas: {language.upper().isupper()}') # -> True 

# .LOWER Pasa a mínusculas, islower Pasa True si estan en minusculas y no False
print(f'Comprueba si todas son Minusculas: {language.lower().islower()}') # -> True