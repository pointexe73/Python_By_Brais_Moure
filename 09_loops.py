### LOOPS ###

# while 
print("LOOPS WHILE")
my_condition = 0

while my_condition < 10:
    print(my_condition) # -> 0 1 2 3 4 5 6 7 8 9 
    my_condition += 1
    if my_condition == 10:
        print("Mi condicion es 10") # -> Mi condicion es 10    

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion") # -> Se detiene la ejecucion
        break # Al verificar que es 15 se detiene la ejecucion
    
    print(my_condition) # -> 11 12 13 14
  
print("La ejecucion continua\n") # -> La ejecucion continua

# for
print("LOOPS FOR\n")

my_list = [35, 24, 62, 52, 30, 31, 17] 

for element in my_list:
    if element == 30:
        continue # -> Al verificar que es 30, se salta la iteracion y continua con la siguiente
    print(f'Elemento en la lista: {element}') # -> 35 24 62 52 31  17
        
print("La ejecucion continua\n") # -> La ejecucion continua