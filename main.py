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
def menuPrincipal():#Este es el menu principal, metodo del cual arranca el programa
    while True:
        print("============MENÚ PRINCIPAL===========")
        print("1. Gestionar Libros")
        print("2. Gestionar Autores")
        print("3. Salir")
        entrada = input("Ingrese la opción: ")

        if entrada == "1":
            menuLibros()#Se tienen un menu de libros
        elif entrada == "2":
            menuAutores()#Se tiene un menu de autores
        elif entrada == "3":
            exit()
        else:
            print("La entrada es incorrecta.")


def menuLibros():
    while True:
        print("============ MENÚ LIBROS =========")
        print("1. Leer")#Permite leer un libro de un autor desde la consola
        print("2. Adicionar Texto")#Esta opción agrega texto al final del archivo
        print("3. Listar libros por Autor")#Lista libros segun Autor de la A-Z
        print("4. Editar Metadatos")#Edita los metadatos de un libro, solo el nombre del libro y en su archivo
        print("5. Adicionar Libro")#Adiciona un libro y permite adicionar texto
        print("6. Eliminar Libro")#Elimina el libro
        print("7. Menú principal")#Retorna al menu principal
        print("8. Salir")
        entrada = input("Ingrese la opción: ")
        if entrada == "1":
            leer()
        elif entrada == "2":
            addTextoLibro()
        elif entrada == "3":
            listarLibrosPorAutor()
        elif entrada == "4":
            editarMetadatos()
        elif entrada == "5":
            add_libros()
        elif entrada == "6":
            del_libros()
        elif entrada == "7":
            menuPrincipal()
        elif entrada == "8":
            exit()
        else:
            print("La entrada es incorrecta.")

def menuAutores():
    while True:
        print("=========== MENÚ AUTORES =========")
        print("1. Editar")#Permite cambiar el nombre del autor, y realiza el cambio en sus libros tambien
        print("2. Eliminar")#Elimina el Autor junto con sus libros
        print("3. Menú principal")#retorna al menu principal
        print("4. Salir")
        entrada = input("Ingrese la opción: ")
        if entrada == "1":
            editarAutor()
        elif entrada == "2":
            eliminarAutor()
        elif entrada == "3":
            menuPrincipal()
        elif entrada == "4":
            exit()
        else:
            print("La entrada es incorrecta.")

#------------------------------------------------------------------Fin Menús


def editarMetadatos():
    oldTitulo = input("Ingrese el antiguo titulo: ")
    newTitulo = input("Ingrese el nuevo titulo: ")
    autor = input("Ingrese el autor: ")

    if (os.path.isdir(autor)):
        if(os.path.isfile(RUTA+autor+"/"+oldTitulo+".txt")):#---la funcion os.path.isfile confirma si es un archivo o no
            libro_nuevo = open(RUTA + autor + "/" + oldTitulo+".txt", "r")  # se abre para escritura con reemplazo
            texto = libro_nuevo.read()  # Se obtiene todo el texto del libro
            texto = texto.replace(" Titulo libro: "+oldTitulo," Titulo libro: "+newTitulo)  # Se reemplaza el el titulo por el nuevo
            libro_nuevo.close()  # se cierra el archivo

            libro_nuevo = open(RUTA + autor + "/" + oldTitulo+".txt", "w")  # se abre para escritura con reemplazo
            libro_nuevo.write(texto)  # Se ingresa el nuevo texto arreglado el cual reemplaza el del actual archivo
            libro_nuevo.close()  # se cierra el archivo
            os.rename(RUTA + autor + "/" + oldTitulo+".txt", RUTA + autor + "/" + newTitulo+".txt")#Finalmente se cambia el nombre al archivo

        else:
            print("El libro NO existe!")
    else:
        print("El autor NO existe! ")


def editarAutor():
    oldAutor=input("Ingrese el viejo Autor: ")
    newAutor=input("Ingrese el nuevo Autor: ")
    if(os.path.isdir(oldAutor)):
        os.renames(oldAutor, newAutor)#Se renombra la carpeta al nuevo autor
        for j in os.listdir(RUTA+newAutor):#Se recorre todos los libros del autor para cambiarle el nombre a cada uno
            libro_nuevo = open(RUTA+newAutor+"/"+j, "r+")#se especifica la ruta de cada libro
            texto = libro_nuevo.read()                              #Se obtiene todo el texto del libro
            texto = texto.replace(" Autor: "+oldAutor, " Autor: "+newAutor) #Se reemplaza el nombre por el nuevo
            libro_nuevo.close()#se cierra el archivo

            libro_nuevo = open(RUTA+newAutor+"/"+j, "w")#se abre para escritura con reemplazo
            libro_nuevo.write(texto)#Se ingresa el nuevo texto arreglado el cual reemplaza el del actual archivo
            libro_nuevo.close()#se cierra el archivo
    else:
        print("El autor NO existe! ")

def eliminarAutor():
    autor = input("Ingrese el Autor: ")
    if(os.path.isdir(autor)):#Se eliminara la carpeta del Autor junto con sus libros
        for j in os.listdir(RUTA+autor):#Se recorre todos los libros para removerlos uno por uno
            os.remove(RUTA + autor+"/"+j)#Direccion completa de cada archivo
        os.rmdir(RUTA+autor)#Finalmente se elimina la carpeta vacia
        print("Se eliminó el Autor y sus libros con exito!")
    else:
        print("El autor NO existe!")

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
    Autores.sort()#Ordena los autores de la A-Z
    for i in Autores:
        if(os.path.isdir(RUTA+i+"/")):# Confirma si está la carpeta
            print("Autor: "+i)#Imprime Autor
            for j in os.listdir(RUTA+i):
                print("    "+j)#Imprime sus libros

def leer():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    if (os.path.isdir(RUTA + autor+"/")):#Comprueba si existe el autor
        if(os.path.isfile(RUTA + autor+"/"+titulo+".txt")):#Comprueba si existe el libro
            libro_nuevo = open(RUTA+autor+"/"+titulo+".txt", "r+")
            texto = libro_nuevo.read()#Obtiene todo el texto del archivo
            print(texto)
            libro_nuevo.close()
        else:
            print("El libro NO existe!")
    else:
        print("El autor NO existe! ")

#--------incio main
menuPrincipal() #El metodo que inicia el programa
#--------fin main