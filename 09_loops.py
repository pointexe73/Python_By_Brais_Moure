### LOOPS ###

# WHILE 
print("LOOPS WHILE")
my_condition = 0

while my_condition < 10:
    print(my_condition) 
    # -R -> 0 1 2 3 4 5 6 7 8 9 
    my_condition += 1
    if my_condition == 10:
        print("Mi condicion es 10") 
        # -R -> Mi condicion es 10    

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion") 
        # -R -> Se detiene la ejecucion
        break # -C -> Al verificar que es 15 se detiene la ejecucion
    
    print(my_condition) 
    # -R -> 11 12 13 14
  
print("La ejecucion continua\n") 
# -R -> La ejecucion continua

# FOR
print("LOOPS FOR\n")

my_list = [35, 24, 62, 52, 30, 31, 17] 

for element in my_list:
    if element == 30:
        continue # -C -> Al verificar que es 30, se salta la iteracion y continua con la siguiente
    print(f'Elemento en la lista: {element}') 
    # -R -> 35 24 62 52 31  17
        
print("La ejecucion continua\n") 
# -R -> La ejecucion continua