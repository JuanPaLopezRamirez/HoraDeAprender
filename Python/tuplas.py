# tuplas

# las tuplas no son mutables

mi_tupla = tuple()
mi_otra_tupla= ()

mi_tupla = (23, 1.65, "Lopez", "Juan")
mi_otra_tupla = ('xd','xd','xd')
print(mi_tupla)
print(mi_tupla[3])



print(mi_tupla.count("Lopez"))
print(mi_tupla.index("Juan"))


# Se puede sumar o combinar tuplas en una nueva
mi_nueva_tupla = mi_tupla + mi_otra_tupla
print(mi_nueva_tupla)

# slice en tuplas
print(mi_nueva_tupla[3:6])


# cambiando el tipo de tupla a lista
mi_otra_tupla = list(mi_otra_tupla)
print(type(mi_otra_tupla))

# borrar una tupla
una_tupla = ("vamos","a","borrar","esta","tupla")
del una_tupla # eliminamos la tupla

