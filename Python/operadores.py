#  Operadores en python

'''
Este es un tema muy sencillo ya que lo normal es usar
los operadores de resta, suma, multiplicacion etc..
pero los vamos a repasar porque nunca esta mal repasar
'''

print(3 + 4)  # 7
print(3 - 4)  # -1
print(3 * 4)  # 12
print(3 / 4)  # 0,75
print(10 // 2) # 5
print(10 % 2)  # 0
print(3 ** 4) # 81

print('hola'+'como'+'estas')
print('Hola'+ str(5))
print('Hola'* 5)

my_float = 2.5 * 2
print('Hola '* int(my_float))

print(3 > 4) # False
print(3 < 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True

# OPERADORES LOGICOS

print( 3 > 4 and 4 < 5)
print( 3 > 1 or 10 < 9)
print(not( 3 < 4)) # es true pero el not lo vuelve falso