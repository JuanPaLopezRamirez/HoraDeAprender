## Clases ##

# class MyPerson:
#   def __init__(self,name,lastname):
#     self.name = name
#     self.lastname = lastname

# mi_persona = MyPerson("Juanpa","Loepz")
# print(mi_persona.name)


class MyPerson:
  def __init__(self,name,lastname, alias="Sin alias"):
    self.full_name = f'{name} {lastname} alias {alias}'
    self.__name = name #propiedad privada
    self.__lastname = lastname #propiedad privada

  def get_name(self):
    return self.__name

  def walk(self):
    print(f"{self.full_name} esta caminando")

mi_persona = MyPerson("Juanpa","Lopez")
print(mi_persona.full_name)
#print(mi_persona.__name) # da error porque esta privado
print(mi_persona.get_name())
mi_persona.walk()

otra_persona = MyPerson("Alejandro","Ramirez","El pepe")
print(otra_persona.full_name)
otra_persona.walk()