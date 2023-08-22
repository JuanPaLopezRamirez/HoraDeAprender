## Expresiones Regulares ##

import re

# match
# El match, encuentra la ocurrrencia si esta esta al principio
mi_string = "Esta es la seccion de Expresiones regulares (expresiones) 23"
otro_string = "Este es un string cualquiera"

print(re.match("Esta es la seccion",mi_string)) # lo encuentra solo si es al inicio
print(re.match("Esta es la seccion",otro_string))


# search
# El search, encuentra la ocurrencia en cualquier parte
search = re.search("expresiones",mi_string)
print(search)

start, end = search.span()
print(mi_string[start:end])


# findall
#El findall, encuentra la ocurrencia en cualquier parte y ademas nos muestra cuantas veces esta
findall = re.findall("expresiones",mi_string)
print(findall)


# split
# El split nos crea una lista, dividiendo los items segun el parametro que le pasemos como (" ")
print(re.split(" ", mi_string))


# sub
# nos remplaza una cosa por otra
print(re.sub("expresiones","Expresiones",mi_string))
print(re.sub("[E|e]xpresiones","EXPRESIONES",mi_string))



# Patterns
# patrones de expresiones regulares

pattern = r"[Ee]xpresiones"
print(re.findall(pattern,mi_string))

pattern = r"[Ee]xpresiones|seccion"
print(re.findall(pattern,mi_string))


pattern = r"[a-z]"
print(re.findall(pattern,mi_string))

pattern = r"[0-9]"
print(re.findall(pattern,mi_string))

pattern = r"\d"
print(re.findall(pattern,mi_string))

pattern = r"\D"
print(re.findall(pattern,mi_string))


email = "juanpa.lopez@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))