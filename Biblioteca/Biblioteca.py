import json
import os

def crear_Json():
    with open('biblioteca.json' ,mode='a') as archivoJson:
#Nuevo Libro
nuevo_libro = {
"id":len(datos["libro"]) +1,
        "nombre":
input('ingrese el nombre del libro: '),
}

def editar_Json():
    with open('biblioteca.json', mode='r') as file:
            lectura = json.load(file)
            idInput =
    int(input("ingrese la id que desea modificar: "))
    for libro in lectura ["libro"]:
         idInput

str(input("ingresa el nuevo nombre"))
id
int(input("ingresa el nuevo ID"))

#eliminar
def borrar_categoria():
     with open ("bilbioteca.json",
                mode= 'r') as file:
          lector = json.load(file)
          idInput = int(input("ingrese categoria que desea eliminar"))
          categoria_a_eliminar = None
for categoria in lector ["categoria"]:
     if categoria ["id"] == id_input:
          categoria_a_eliminar = categoria
          break
     if categoria_a_eliminar: 
          lector["Categorias"].remove ('categoria_a_eliminar')
     else:
          print("Categoria no encontrada.")  




def buscar():
    with open("biblioteca.json" mode="r")






