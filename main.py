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

#--------------------------------------------------------Incio Menús
def menuPrincipal():
    while True:
        print("1. Gestionar Libros")
        print("2. Gestionar Autores")
        print("3. Salir")
        entrada = input("Ingrese la opción: ")

        if entrada == "1":
            menuLibros()
        elif entrada == "2":
            menuAutores()
        elif entrada == "3":
            exit()
        else:
            print("La entrada es incorrecta.")


def menuLibros():
    while True:
        print("1. Leer")
        print("2. Adicionar Texto")
        print("3. Adicionar Libro")
        print("4. Eliminar Libro")
        print("5. Regresar atrás")
        print("6. Salir")
        entrada = input("Ingrese la opción: ")
        if entrada == "1":
            pass
        elif entrada == "2":
            pass
        elif entrada == "3":
            pass
        elif entrada == "4":
            pass
        elif entrada == "5":
            menuPrincipal()
        elif entrada == "6":
            exit()
        else:
            print("La entrada es incorrecta.")

def menuAutores():
    while True:
        print("1. Editar")
        print("2. Eliminar")
        print("3. Regresar atrás")
        print("4. Salir")
        entrada = input("Ingrese la opción: ")
        if entrada == "1":
            pass
        elif entrada == "2":
            pass
        elif entrada == "3":
            menuPrincipal()
        elif entrada == "4":
            exit()
        else:
            print("La entrada es incorrecta.")

#------------------------------------------------------------------Fin Menús


#------------------------------------------------------------------Inicio Métodos del Profesor
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

def addMetadatos(titulo, autor):
    texto=" Autor :"+autor+"\n"
    texto=texto+"Tutulo libro:" + titulo+"\n"
    texto = texto + "País: Colombia \n"
    texto = texto + "Año: 2019 \n"
    texto = texto + "_________________________________________________________________________________________\n"
    return texto
#---------------------------------------------------------------------Fin Métodos del Profesor


#--------incio main
menuPrincipal()
#add_libros("Programacion en Python1","pepe")
#--------fin main