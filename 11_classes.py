### CLASSES ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
# -R -> <__main__.MyEmptyPerson object at 0x7f82800b7d30>
print('----------------------\n')

print('Clase 1')

class Person:
    # -C -> Constructor de la clase, se ejecuta al crear un objeto
    def __init__(self, name, surname):
        # -C -> Se asignan los valores de los parámetros a los atributos del objeto
        self.name = name
        self.surname = surname
    
my_person = Person('John', 'Doe')
print(f'My name is -> {my_person.name} {my_person.surname}')
# -R -> My name is -> John Doe

print('----------------------\n')

print('Clase 2')

class Person:
    # -C -> Constructor de la clase, se ejecuta al crear un objeto
    def __init__(self, name, surname):
        # -C -> Se crea el atributo full_name concatenando name y surname
        self.full_name = f'{name} {surname}'
        
my_person = Person('John', 'Doe')
print(f'My name is -> {my_person.full_name}')
# -R -> My name is -> John Doe

print('----------------------\n')

print('Clase 3')

class Person:
    # -C -> Constructor de la clase, se ejecuta al crear un objeto
    def __init__ (self, name, surname):
        # -C -> Se crea el atributo full_name concatenando name y surname
        self.full_name = f'{name} {surname}'
    
    # -C -> Método de la clase, se puede llamar desde un objeto
    def walk (self):
        # -C -> Se imprime un mensaje que indica que la persona está caminando
        print(f'{self.full_name} is walking')
    
my_person = Person('John', 'Doe')

my_person.walk()
# -R -> John Doe is walking