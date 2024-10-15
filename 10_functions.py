### FUNCTIONS ###

print("Funcion 1")
print("---------------\n") 

# Funcion 1
def my_function():
    print(f'Resultado -> {"Esto es una funcion"}') 
    
    
my_function()
# -R -> Esto es una funcion

def sum_two_values(first_number, second_number):
    print(f'Resultado de la suma -> {first_number + second_number}')
    
sum_two_values(2,2)
# -R -> 4
 
# -C -> Forza 2 parametros de tipo int para la funcion
sum_two_values(int("2"),int("2"))
# -R -> 4

print()
print("Funcion 2")
print("---------------\n")

# Funcion 2
# -C -> Con return para poder usar el resultado en otras partes del codigo
def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10,5)
print(f'Resultado de la suma -> {my_result}')
# -R -> 15 

print()
print("Funcion 3")
print("---------------\n")

# Funcion 3
def print_name(name, surname):
    print(f'Resultado -> {name} {surname}')
    
print_name(surname="Moure", name="Brais")
# -R -> Brais Moure

print()
print("Funcion 4")
print("---------------\n")

# Funcion 4
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f'Resultado -> {name} {surname} {alias}')
    
print_name_with_default("Brais", "Moure", "MoureDev")

print()
print("Funcion 5")
print("---------------\n")

# Funcion 5
# -C -> *args -> Permite pasar un numero indeterminado de parametros, los parametros se guardan en una tupla
def print_texts(*texts):
    print(texts)
    
print_texts("Hola", "Python", "Brais")
# -R -> ('Hola', 'Python', 'Brais')

print()
print("Funcion 6")
print("---------------\n")

# Funcion 6

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts("Hola", "Python", "Brais")
# -R -> HOLA
# -R -> PYTHON
# -R -> BRAIS

print_upper_texts("Hola")
# -R -> HOLA