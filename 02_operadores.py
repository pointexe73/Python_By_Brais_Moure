### OPERADORES ARITMETICOS ###

''' Operaciones con enteros '''
# Suma
print(f'Suma -> {3 + 4}') 
# Resta
print(f'Resta -> {3 - 4}')
# Multiplicación
print(f'Multiplicacion -> {3 * 4}')
# Division
print(f'Division -> {3 / 4}')
# Residuo o Resto
print(f'Residuo o Resto -> {10 % 3}')
# Division Entera o Cociente
print(f'Division Entera o Cociente -> {10 // 3}')
# Potencia
print(f'Potencia -> {3 ** 4}')
print() # PRINT Vacio para hacer un salto de linea el la consola


''' Operaciones con cadenas de texto '''
# Concatenando cadenas de texto
print('Hola ' + 'Python ' + '¿Que tal?')
# Contantenar una cadena y un numero, se utiliza str() para pasar (5) a cadena de texto
print('Hola ' + str(5))
# Se Multpica ('Hola') 8 veces
print('Hola ' * (2 ** 3))
print()

''' Operaciones Mixtas '''
# Se Multiplico 2.5 * 2 y se convirtio a entero con int() para poder multiplicarlo con la cadena de texto ('Hola')
my_float = 2.5 * 2
print("Hola " * int(my_float)) 
print()

### OPERADORES COMPARATIVOS ###

''' Operaciones con enteros '''

# Mayor que...
print(3 > 4)  
# Menor que...
print(3 < 4)
# Mayor o igual que...
print(3 >= 4)
# Menor o igual que...
print(3 <= 4)
# Igual que...
print(3 == 4)
# Diferente que...
print(3 != 4)
print()

''' Operaciones con cadenas de texto '''

'''
    Se compara la posicion de las letras en el abecedario,
    si la primera letra de la primera cadena es menor que
    la primera letra de la segunda cadena, el resultado es True,
    si no, el resultado es False
'''

# Mayor que...
print(f'El resultado es = {"Hola" > "Python"}')

# Menor que...
print(f'El resultado es = {"Hola" < "Python"}')

# Mayor o igual que...
print(f'El resultado es = {"Hola" >= "Python"}')

# Menor o igual que...
print(f'El resultado es = {"Hola" <= "Python"}')

# Igual que...
print(f'El resultado es = {"Hola" == "Python"}')

# Diferente que...
print(f'El resultado es = {"Hola" != "Python"}')

print()

### OPERADORES LOGICOS ###

# 3 > 4 es False y "Hola" > "Python" es False = False and False = Falsej
print(f'False and False = {3 > 4 and "Hola" > "Python"}')

# 3 > 4 es False y "Hola" > "Python" es False = False or False = False
print(f'False or False = {3 > 4 or "Hola" > "Python"}')

# 3 < 4 es True y "Hola" < "Python" es True = True and True = True
print(f'True and True = {3 < 4 and "Hola" < "Python"}')

# 3 < 4 es True y "Hola" < "Python" es True = True or True = True
print(f'True or True = {3 < 4 or "Hola" < "Python"}')

# 3 < 4 es True y "Hola" < "Python" es True y 4 == 4 es True = True or (True and True) = True or True = True
print(f'True or (True and True) = {3 < 4 or ("Hola" < "Python" and 4 == 4)}')

# 3 > 4 es False = not(False) = True
print(f'not False = {not(3 > 4)}')