
## Condicionales ##

mi_condicion = True

if mi_condicion:
  print("Se ejecuta la condicion del if")

print("La ejecucion continua")


condicion = 20
# nacionalidad = "Colombiano"
nacionalidad = "Estadounidense"

if condicion >= 18 and nacionalidad == "Colombiano":
  print("Eres mayor de edad")
elif condicion >= 20 and nacionalidad == "Estadounidense":
  print("Eres mayor de edad en Estados Unidos")
else:
  print("Eres menor de edad")

print("El programa continua")


if not False:
  print("Es false")
else:
  print("Es True")

