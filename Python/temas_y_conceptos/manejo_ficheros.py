## Manejo de Ficheros ##

# .txt file

# tenemos que leer desde el directorio raiz, por eso empezamos con Python
#txt_file =open('Python/temas_y_conceptos/textFile.txt',"r+") # r+ = leer y escribir
#print(txt_file.read())
# txt_file.write('''Mi nombre es Juan Pablo
# Mis apellidos son Lopez Ramirez
# tengo 23
# vivo en el pais de Colombia
# naci en Pereira
# ''')
#print(txt_file.read(10)) # leemos 10 caracteres mas
#print(txt_file.readline())

# for line in txt_file.readlines():
#   print(line)

# txt_file.write("Vamos Depor")
# print(txt_file.read())
# txt_file.close()



#import os
#os.remove('Python/temas_y_conceptos/textFile.txt')  #asi borrariamos el fichero

# .json file
import json

json_file = open('Python/temas_y_conceptos/mi_json.json','w+')

json_test ={
  "Nombre":"Pepito",
  "Apellidos":"Perez",
  "edad":18,
  "language": "JavaScript"
}

# {
#   "Nombre":"Juan Pablo",
#   "Apellidos":"Lopez Ramirez",
#   "edad":23,
#   "language": "Python"
# }

json.dump(json_test,json_file, indent=4)

json_file.close()

with open('Python/temas_y_conceptos/mi_json.json') as mi_otro_json:
  for line in mi_otro_json.readlines():
    print(line)

#convertimos de json a diccionario
json_dicc = json.load(open('Python/temas_y_conceptos/mi_json.json'))
print(json_dicc)
print(json_dicc['Nombre'])