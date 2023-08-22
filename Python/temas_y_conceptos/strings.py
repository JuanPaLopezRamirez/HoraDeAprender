# STRINGS

mi_string= "esto es un string"
otro_string = "Lo mismo de arriba xd"

print("Quiero concatenar los strings: ",mi_string,"",otro_string)

mi_nuevo_string = 'Esto va a ser un string con salto \n saltamos'
print(mi_nuevo_string)

con_tabulacion = '\tEste string tiene tabulacion'
print(con_tabulacion)


# Formateo

name, lastname, age = 'Juanpa','Lopez Ramirez', 23
print('Mi nombre es {} {} y mi edad es {}'.format(name,lastname,age))
print('Mi nombre es %s %s y mi edad es %d' %(name,lastname,age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")


#Desempaquetado de caracteres
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)

# division de strings algo asi

strings_divididos = language[1:3] # nos devuelve (yt)
print(strings_divididos)

strings_divididos = language[1:] # nos devuelve (ython)
print(strings_divididos)

strings_divididos = language[-2] # nos devuelve la (o)
print(strings_divididos)

# inverso
lenguaje_inverso = language[::-1] #asi le damos la vuelta
print(lenguaje_inverso)


print(language.capitalize())
print(language.upper())
print(language.count("h"))
print(language.isnumeric())
print(language.isdecimal())
print(language.lower().isupper())