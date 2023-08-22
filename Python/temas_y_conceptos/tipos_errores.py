## Tipos de Errores en Python ##

# SyntaxisError
#print Hola mundo # Erro
print('Hola mundo')


# NameError
name = 'Juan Pablo lopez' #Error si no definimos name
print(name)


#IndexError
mi_lista = [1,2,3,4,5]
print(mi_lista[0])
print(mi_lista[-1])
print(mi_lista[3])
#print(mi_lista[5]) # Error porque el indice 5 no existe


# ModuleNotFoundError
#import maths # Error porque la libreria maths no existe
import math


# AttributeError
# print(math.PI) #Error porque el atributo PI no existe
print(math.pi)


#KeyError
mi_diccionario = {'Nombre':'Juan Pablo','Apodo':'Juanpa','edad':23}
#print(mi_diccionario[0]) #Error porque cero no es una key valida
print(mi_diccionario['Nombre'])


# TypeError
#print(mi_lista["0"]) # Error porque las listas no aceptan str
print(mi_lista[0])


# ValueError
mi_entero = int("10 dias") #Error porque no podemos transformarlo a un entero
mi_entero = int("10")
print(mi_entero)