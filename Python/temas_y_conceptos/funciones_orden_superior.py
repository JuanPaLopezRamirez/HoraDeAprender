## Funciones de Orden Superior ##

# son funciones dentro de funciones

def sumar_uno(value):
  return value + 1

def sumar_valores(num1,num2):
  return num1 + num2

def ejemplo(value1, value2):
  return sumar_uno(value1 + value2)

print(ejemplo(5,5))

def ejemplo2(value1,value2, funcion):
  return funcion(value1+value2)

print(ejemplo2(5,4,sumar_uno))

## Closures ##

#los closures retornan una funcion

def sum_ten():
  def add(value):
    return value + 10
  return add

add_closure =sum_ten()
print(add_closure(5))

print(sum_ten()(5))


## Funciones de Orden Superior del Lenguaje ##

numbers = [2,5,10,23,19]

def mult_por2(number):
  return number * 2

def filtrar_mayor_diez(number):
  if(number > 10):
    return True
  return False

#Map
print(list(map(mult_por2,numbers)))
print(list(map(lambda number: number*2,numbers)))


#Filter
print(list(filter(filtrar_mayor_diez, numbers)))

#Reduce



