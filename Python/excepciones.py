## Excepciones ##

numero1 = 20
numero2 = 30
# numero2 = "30"

try:
  print(numero1 + numero2)
  print("No se ha producido un error")
except:
  print("Se ha producido un error :( ")


# tambien podemos usar el try except else
num1 = 5
num2 = 5

try:
  print(num1 + num2)
  print("No se ha producido un error")
except:
  print("Se ha producido un error :( ")
else: #se ejecuta si no se produce una excepcion
  print("No se produjo una excepcion porque no hubo un error")


# tambien podemos usar el finally al final

# captura de excepciones por tipo
sumando1 = 3
sumando2 = "1"

try:
  print(sumando1 + sumando2)
  print("No se ha producido un error")
except TypeError: # un error de tipo TypeError
  print("Se ha producido un error al sumar enteros con algo que no era un entero")

# si queremos ser mas especificos ponemos varios tipos de errores
numero1 = 20
numero2 = "30"

try:
  print(numero1 + numero2)
  print("No se ha producido un error")
except ValueError:
  print("Se ha producido un error de tipo ValueError")
except TypeError:
  print("Se ha producido un error de tipo TypeError ")


# tambien podemos imprimir los errores y la informacion de la excepcion
numero1 = 20
numero2 = "30"
try:
  print(numero1 + numero2)
  print("No se ha producido un error")
except TypeError as error: #capturamos el error
  print('\n Se produjo un error de tipo Error ->',error)
except Exception as excepcion:
  print('\nLa informacion de la excepcion es->',excepcion)