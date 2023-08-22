## Ejercicio 3: La sucesion de Fibonacci

def fibonacci():
  prev = 0
  next = 1
  for index in range (0,50):
    print(prev)

    fib = prev + next
    prev = next
    next = fib

fibonacci()