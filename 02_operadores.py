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


''' Operaciones con cadenas de texto '''
# Concatenando cadenas de texto
print('Hola ' + 'Python ' + '¿Que tal?')
# Contantenar una cadena y un numero, se utiliza str() para pasar (5) a cadena de texto
print('Hola ' + str(5))
# Se Multpica ('Hola') 8 veces
print('Hola ' * (2 ** 3))

''' Operaciones Mixtas '''
# Se Multiplico 2.5 * 2 y se convirtio a entero con int() para poder multiplicarlo con la cadena de texto ('Hola')
my_float = 2.5 * 2
print("Hola " * int(my_float)) 

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

''' Operaciones con cadenas de texto '''

'''
    Se compara la posicion de las letras en el abecedario,
    si la primera letra de la primera cadena es menor que
    la primera letra de la segunda cadena, el resultado es True,
    si no, el resultado es False
'''

# Mayor que...
print("Hola" > "Python")
# Menor que...
print("Hola" < "Python")
# Mayor o igual que...
print("Hola" >= "Python")
# Menor o igual que...
print("Hola" <= "Python")
# Igual que...
print("Hola" == "Python")
# Diferente que...
print("Hola" != "Python")

### OPERADORES LOGICOS ###
2.18.24