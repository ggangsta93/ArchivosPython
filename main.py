##Sistema de gestion de archivos de biblioteca
import os
###Complementar el trabajo así
###HAcer gestion de autores y libros
###la gestion debe permitir, 1 agregar texto a los libros
### listar libros por autor
### leer un determinado libro
###
RUTA ="/home/javier/PycharmProjects/Biblioteca/"
##-----------------Este metodo crea una carpeta para cada autor, si el autor ya existe
##-----Crea los libros en su carpeta
##---Si un autor y un libro ya existe, el sistema notifica que ese libro ya existe
##---Cuando no existe el autor ni el libro, se crean la carpeta del autor y dentro de ella el libro
def add_libros(titulo, autor):
    carpeta_autor=RUTA+autor+"/"
    if(os.path.isdir(carpeta_autor)):## la funcio os.path.isdir confirma si es directorio o no
        if(os.path.isfile(carpeta_autor+titulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
             print("El libro ya existe")
        else:
            libro_nuevo = open(carpeta_autor + titulo + ".txt", "a+")
            libro_nuevo.write(agregar_texto())
            libro_nuevo.close()
    else:
        os.mkdir(RUTA+autor)
        libro_nuevo = open(carpeta_autor + titulo + ".txt", "a+")
        libro_nuevo.write(addMetadatos(titulo, autor)+agregar_texto())
        libro_nuevo.close()

def agregar_texto():
    texto="fin"
    dato=""
    salida=""
    i=0
    while texto!=dato:
        dato=input("Para salir fin, Digite el texto del libro")
        salida=salida+dato+"\n"
    return salida


add_libros("Programacion en Python1","pepe")





def addMetadatos(titulo, autor):
    texto=" Autor :"+autor+"\n"
    texto=texto+"Tutulo libro:" + titulo+"\n"
    texto = texto + "País: Colombia \n"
    texto = texto + "Año: 2019 \n"
    texto = texto + "_________________________________________________________________________________________\n"
    return texto