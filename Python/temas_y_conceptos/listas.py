# Listas

mi_lista = [] #esto es una lista
mi_segunda_lista = list() # esto tambien es una lista

print(len(mi_lista))
print(len(mi_segunda_lista)) #como esta vacia tiene 0 elementos

mi_lista = [35,24,62,17,23]
print(len(mi_lista))
print(mi_lista)
print(mi_lista[-1]) # devuelve el ultimo 23
print(mi_lista.count(35))# nos devuelve la cantidad de 35 que hay


otra_lista = ["hola","como","estas","amigo"]

# asi podemos unir listas
lista_unificada = mi_lista + otra_lista
print(lista_unificada)

# append: para agregar nuevos elementos a la lista
lista_unificada.append("Agregando")
print(lista_unificada)

# insert: para insertar un elemento en algun punto de la lista
lista_unificada.insert(0,"Posicion1")
print(lista_unificada)

# remove: para remover un elemento de la lista
lista_unificada.remove("estas")
print(lista_unificada)# elimina la palabra (estas) pero solo la primera vez que aparece


# copy: sirve para copiar los valores de una lista
mi_nueva_lista = lista_unificada.copy()
print("Nueva lista:",mi_nueva_lista)
lista_unificada.clear()
print("Lista unificada despues del clear: ",lista_unificada)
lista_unificada = mi_nueva_lista.copy()
print("Lista unificada despues del copy: ",lista_unificada)


# sort: ordena

lista_numerica = [1,2,3,4,5]
lista_numerica.reverse()
print(lista_numerica)
lista_numerica.sort()
print(lista_numerica)