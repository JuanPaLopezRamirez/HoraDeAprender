
#variables

# en python deberiamos usar snake_case para nombrar variables

my_variable = "Mi variable de tipo string"
print(my_variable)

my_numvar = 10
print(my_numvar)

my_boolvar = True
print(my_boolvar)


print('Hola',',','mundo','.','Como estan todos','!')


#como cambiar una variable de tipo entero a string

my_example = 19
my_string = str(my_example)
print(my_string)
print(type(my_string))


# usamos len para ver la cantidad de caracteres de una cadena

usando_len = 'vamos colombia'
print(len(usando_len)) #14 caracteres, incluye el espacio


# mas ejemplos

my_nombre = 'Juan Pablo Lopez Ramirez'
print('Mi nombre es: ', my_nombre)
print('Mi nombre es: '+ my_nombre)

# declarar e inicializar variables en una sola linea

name, lastname,age = 'Juan Pablo', ' Lopez', 23
print('Mi nombre es '+name+lastname+' y mi edad es de '+str(age)+' años')


# Uso del Input

name = input('Cual es tu nombre? ')
age  = input('Cual es tu edad: ')

print(name)
print(age)


# forma de especificar el tipo de dato
address: str = 'Mi direccion'
address = 32 # aca le cambiamos el tipo de dato

print(type(address)) # int

