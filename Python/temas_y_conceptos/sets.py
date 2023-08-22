# Sets

mi_set = set()
mi_otro_set = {} #inicialmente es un diccionario

print(type(mi_set))
print(type(mi_otro_set))

mi_otro_set = {"juan","pablo","lopez","ramirez"} #ahora es un set
print(type(mi_otro_set))

mi_otro_set.add("JUANPALOPEZ1")
print(mi_otro_set) # un set no es una estructura ordenada


mi_otro_set.add("JUANPALOPEZ1")
print(mi_otro_set) # un set no admite repetidos

# encontrar un elemento en un set
print("juan" in mi_otro_set) # me devuelve true

# remove y clear
mi_otro_set.remove("JUANPALOPEZ1") # remueve el valor que le pasamos
print(mi_otro_set)
mi_otro_set.clear() # elimina todos los del set
print(len(mi_otro_set))

# crear un set a partir de otros
set1 = {"set","de","ejemplo"}
set2 = {"otro","set"}

new_set = set1.union(set2)
print(new_set) # recordemos que los set no aceptan valores repetidos