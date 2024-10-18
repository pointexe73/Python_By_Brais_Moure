### EXCEPTIONS ###

print("1 (try-except)")
print("---------------------")
numberOne = 5
numeberTwo = "1"

# -c -> Se ejecuta except
try:
    print(numberOne + numeberTwo)
    print("No se ha producido un error")
    
except:
    # -c -> Se ejecuta si se produce una excepcion
    print("Se ejecuta una except")
    # -r -> Se ejecuta una except

print()    
print("2 (try-except-else)")
print("---------------------")

numberThree = 5
numberFour = 1

# -c -> Se ejecuta try y else. Se ejecuta si no se produce una excepcio
try:
    print(f'Se ejecuta try -> {numberThree + numberFour}')
    # -r -> Se ejecutra try 6

except :
    print("Se ha producido un error")
    
else:
    # -c  -> Se ejecuta si no se produce una excepcion
    print("Se ejecuta else")
    # -r -> La ejecucion continua correctamente
    
print()
print("3 (try-except-else-finally)")
print("---------------------")

numberFive = 5
numberSix = "1"

# -c -> Se ejecuta except y finally siempre se ejecuta
try:
    # -c -> No se ejecuta
    print(numberOne + numeberTwo)
    print("No se ha producido un error")
    
except :
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
    # -r -> Se ha producido un error
    
else:
    # -c -> No se ejecuta
    print("La ejecucion continua correctamente")
   
    
finally:
    # -c -> Se ejecuta siempre
    print("La ejecucion continua")
    # -r -> La ejecucion continua