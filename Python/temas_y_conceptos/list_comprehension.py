## listas comprimidas o algo asi ##


mi_lista_original = [10,20,30,40,50,60,100]

mi_lista = [i for i in mi_lista_original]
print(mi_lista) #[10,20,30,40,50,60,100]

mi_otra_lista = [i for i in range(8)]
print(mi_otra_lista)

tercera_lista = range(8)
print(list(tercera_lista))

otro_ejemplo = [i+1 for i in range(7)]
print(otro_ejemplo)

def sum_five(number):
  return number+5

ultimo_ejemplo = [sum_five(i) for i in mi_lista_original]
print(ultimo_ejemplo)