# Diccionarios

mi_diccionario = dict()
un_diccionario = {}

print(type(mi_diccionario))

un_diccionario = {'Nombre':'Juan Pablo','Apellidos':'Lopez Ramirez','edad':23}

print(un_diccionario)

un_diccionario["Carrera"] = "Ingenieria en Sistemas"
print(un_diccionario)

print(un_diccionario["Carrera"])

del un_diccionario["Carrera"]
print(un_diccionario)

# buscando por clave
print("Juan Pablo" in un_diccionario)
print("Nombre" in un_diccionario)


print(un_diccionario.keys()) # imprime las claves
print(un_diccionario.values()) # imprime los valores