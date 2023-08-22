## Funciones ##

def mi_funcion():
  suma = 2+3
  return suma

#print(mi_funcion())

def sumar(numero1,numero2):
  suma = numero1 + numero2
  print("La Suma da:",suma)

#sumar(10,20)


# si queremos pasarle muchos paramatros
def print_textos(*textos):
  print(textos)

#print_textos("hola","como estan","que hacen","saludos")
