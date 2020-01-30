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
        print("3. Listar libros por Autor")
        print("4. Adicionar Libro")
        print("5. Eliminar Libro")
        print("6. Regresar atrás")
        print("7. Salir")
        entrada = input("Ingrese la opción: ")
        if entrada == "1":
            leer()
        elif entrada == "2":
            addTextoLibro()
        elif entrada == "3":
            listarLibrosPorAutor()
        elif entrada == "4":
            add_libros()
        elif entrada == "5":
            del_libros()
        elif entrada == "6":
            menuPrincipal()
        elif entrada == "7":
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



def agregar_texto():
    texto="fin"
    dato=""
    salida=""
    i=0
    while texto!=dato:
        dato=input("Para salir fin, Digite el texto del libro: ")
        if not "fin" == dato:
            salida=salida+dato+"\n"
    return salida

def addMetadatos(titulo, autor):
    pais = input("Digite Pais: ")
    anio = input("Digite año: ")
    texto =" Autor: "+autor+"\n"
    texto = texto + " Titulo libro: " + titulo+"\n"
    texto = texto + " País: "+pais+" \n"
    texto = texto + " Año: "+anio+" \n"
    texto = texto + "_________________________________________________________________________________________\n"
    return texto

def add_libros():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    carpeta_autor = RUTA + autor+"/"
    if(os.path.isdir(carpeta_autor)):# la funcio os.path.isdir confirma si es directorio o no
        if(os.path.isfile(carpeta_autor+titulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
             print("El libro ya existe!")
        else:
            libro_nuevo = open(carpeta_autor + titulo + ".txt", "a+")
            libro_nuevo.write(addMetadatos(titulo, autor) + agregar_texto())
            libro_nuevo.close()
    else:
        os.mkdir(RUTA+autor)
        libro_nuevo = open(carpeta_autor + titulo + ".txt", "a+")
        libro_nuevo.write(addMetadatos(titulo, autor)+agregar_texto())
        libro_nuevo.close()

def del_libros():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    carpeta_autor = RUTA + autor+"/"
    if(os.path.isdir(carpeta_autor)):# la funcio os.path.isdir confirma si es directorio o no
        if(os.path.isfile(carpeta_autor+titulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
            os.remove(carpeta_autor+titulo+".txt")
        else:
            print("El libro NO existe")

    else:
        print("El autor NO existe")

def addTextoLibro():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    carpeta_autor = RUTA + autor+"/"
    if(os.path.isdir(carpeta_autor)):# la funcio os.path.isdir confirma si es directorio o no
        if(os.path.isfile(carpeta_autor+titulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
            libro_nuevo = open(carpeta_autor + titulo + ".txt", "a+")
            libro_nuevo.write(agregar_texto())
            libro_nuevo.close()
        else:
            print("El libro NO existe!")
    else:
        print("El Autor NO existe!")

def listarLibrosPorAutor():
    Autores = list(filter(os.path.isdir, os.listdir(RUTA)))
    Autores.sort()
    for i in Autores:
        if(os.path.isdir(RUTA+i+"/")):# Confirma si está la carpeta
            print("Autor: "+i)#Imprime Autor
            for j in os.listdir(RUTA+i):
                print("    "+j)#Imprime sus libros

def leer():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    if (os.path.isdir(RUTA + autor+"/")):
        if(os.path.isfile(RUTA + autor+"/"+titulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
            libro_nuevo = open(RUTA+autor+"/"+titulo+".txt", "r+")
            texto = libro_nuevo.read()
            print(texto)
            libro_nuevo.close()

#--------incio main
menuPrincipal()
#--------fin main