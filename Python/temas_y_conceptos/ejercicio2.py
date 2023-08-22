## ejercicio 2 : Anagrama ##

def anagrama(palabra1,palabra2):

  if(palabra1.lower() == palabra2.lower()):
    return 'Las Palabras no son anagramas'

  if sorted(palabra1.lower()) == sorted(palabra2.lower()):
    return 'Las palabras son anagramas'

print(anagrama('amor','roma'))