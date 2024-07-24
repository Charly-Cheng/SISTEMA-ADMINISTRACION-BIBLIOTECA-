"""
1. Estructura logica de Programa para iniciar y unir todos los menu y operacion.

2. Menú de administrador 
    A. Administrar de Usuario
        A.a Crear un Usuario 
        A.b listar todos Usuario
        A.c modificar Rol de Usuario 
        A.d Eliminar Usuario
        A.e Salir de Menu

    B. Administrar de Libro
        B.a. Crear un nuevo libro a la biblioteca.
        B.b. Mostrar todos los libros.
        B.c. Modificar Dato de ibro
        B.d. Eliminar un libro de la biblioteca.
        B.e. Salir de Menu

    
    punto C es Opcionar, puede ampliar en punto B.C Modificar Dato de ibro
    C. Gestion de Préstamos
        C.a Lista de Reserva o pedidos
        C.b lista de libro prestado
        C.c Registrar el préstamo de un libro a un usuario.
        C.d Registrar la devolución de un libro.
        C.e Mostrar los libros prestados a un usuario específico.


3. Menú de usuario 
    a. Buscar libros y Reserva el libro.
    
4. Diseño de interfaz y presentación


"""


import os
import json
import getpass
import datetime
import time
#from mi_paquete.admin_libro import *
# Variables globales

# lista Guardar dato de usuario
usuario_DB = [{"id":"admin", "clave":"admin", "nombre":"Cheng","DNI":"37754754","nivel":2},
            {"id":"admin1", "clave":"admin1", "nombre":"Gabriela Bentos","DNI":"65783622","nivel":2},
            {"id":"admin2", "clave":"admin2", "nombre":"Luis Altgelt","DNI":"73568779","nivel":2},
            {"id":"admin3", "clave":"admin3", "nombre":"Ruth Masters","DNI":"87328798","nivel":2},
            {"id":"lector", "clave":"lector", "nombre":"Charly","DNI":"87321780","nivel":1}
            ]



libro_DB = [{"id":"32456", "titulo":"Señor de Anillo", "autor":"Tolkien","año de edicion":"1955", "Estado":""},
            {"id":"1", "titulo":"Pulp Fiction", "autor":"Quentin Tarantino","año de edicion":"1994","Estado":""},
            {"id": "2", "titulo": "xxx", "año de edicion": "1994", "autor": "Borges","Estado":""},
            {"id": "3", "titulo": "Harry Potter y la Piedra Filosofal", "año de edicion": "2002", "autor": "J.K: Rowling","Estado":""},
            {"id": "4", "titulo": "El Hombre Bicentenario", "año de edicion": "1998", "autor": "Isaac Asimov","Estado":""},
            {"id": "5", "titulo": "El principito", "año de edicion": "1997", "autor": "Antoine de Saint-Exupéry","Estado":""},
            {"id": "6", "titulo": "El Alquimista", "año de edicion": "1996", "autor": "Paulo Coelho","Estado":""},
            {"id": "7", "titulo": "El Quijote", "año de edicion": "1995", "autor": "Miguel de Cervantes","Estado":""},
            {"id": "8", "titulo": "El Señor de los Anillos", "año de edicion": "1994", "autor": "J.R.R: Tolkien","Estado":""},
            {"id": "9", "titulo": "La Iliada", "año de edicion": "1993", "autor": "Homero","Estado":""},
            {"id": "10", "titulo": "La Odisea", "año de edicion": "1992", "autor": "Alfas","Estado":""},
            {"id": "11", "titulo": "La Danza de la Muerte", "año de edicion": "1991", "autor": "George R.R. Martin","Estado":""},

            {"id": "13", "titulo": "El Laberinto de la Soledad", "año de edicion": "2005", "autor": "Gabriel Garcia Marquez","Estado":""},
            ]

archivo_usuario_DB = "usuario_DB.json"
archivo_libro_DB = "libro_DB.json"

lista_archivos_DB = [archivo_usuario_DB, archivo_libro_DB]
lista_DB = [usuario_DB, libro_DB]

# funciones de Menu y operaciones


def guardar_DB(archivo,datos_DB):
    with open (archivo, "w") as file:
        json.dump(datos_DB, file)


def cargar_DB(lista_archivos_DB, lista_DB):
    for i in range(len(lista_archivos_DB)):
        try:
            with open (lista_archivos_DB[i], "r") as file:
                lista_DB[i] = json.load(file)
        except FileNotFoundError:
            guardar_DB(lista_archivos_DB[i],lista_DB[i])
        except json.decoder.JSONDecodeError:
            #  agregando el dia de hoy a archivo existente
            current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            file_name, file_extension = os.path.splitext(lista_archivos_DB[i])
            new_name = f"{file_name}_{current_time}{file_extension}"
            os.rename(lista_archivos_DB[i], new_name)
            guardar_DB(lista_archivos_DB[i],lista_DB[i])
    return lista_DB

def continuar ():
    input("Presione ENTER para continuar...")

def proceso_100 ():
    tarea = " El sistema esta cargando datos"
    tiempo = 3
    n=100            # longitude de la barra
    ico = "\033[1;36;40m" +'█' + "\033[0m"      # caracter de la barra
    print("\033[1;36;40m" + tarea.center(110)  + "\033[0m")
    print ()
    for i in range(n+1):
        print(f'\r[{ico*i}{" "*(n-i)}] {i*100/n}%',end='')
        time.sleep(0.01 * tiempo)


def cabezera ():
    fecha = datetime.datetime.now().date()
    hora = datetime.datetime.now().time()
    print (" ".rjust(145, "-"))
    print("     Sistema de Administración de " "\033[1;36;40m" + "Biblioteca Públic.ar📚 " + "\033[0m" + " ".rjust(68), end = "")
    print (f"Fecha : {fecha.strftime('%d/%m/%y')}")
    print("     Te damos la bienvenida 🤝 a ""\033[1;33;40m" + "Proyecto Grupo Dragon🐉" + "\033[0m" +" ".rjust(70), end = "")
    print (f"Hora : {hora.strftime('%H:%M:%S')}")
    print (" ".rjust(145, "-"))


def espacio():
    print (" "*12, end = "")

def marco_menu():
    print ("-"*50)


def cabezera_menu (zona, usuario):
    espacio()
    marco_menu()
    espacio()
    if usuario["nivel"] == 2:
        print ("Bienvenido Administrador: " + "\033[4;91;40m" + usuario["nombre"] + "\033[0m")
    elif usuario["nivel"] == 1:
        print("Bienvenido Usuario: " + "\033[4;94;40m" + usuario["nombre"] + "\033[0m")
    elif usuario["nivel"] == 0:
        print("Bienvenido Invitado: " + "\033[4;92;40m" + usuario["nombre"] + "\033[0m")
    espacio()
    marco_menu()
    espacio()
    print ("Estas en Menu de  " + "\033[4;32;40m" + zona + "\033[0m")


def longin (usuario_DB):
    os.system('cls')
    cabezera()
    espacio()
    marco_menu()
    espacio()
    print("                      " + "\033[4;32;40m" + "Login" + "\033[0m")
    espacio()
    marco_menu()
    espacio()
    id=input("Ingrese su id: ")
    clave = getpass.getpass("            Ingrese su clave: ")
    
    for indice in range(len(usuario_DB)):
        if usuario_DB[indice]["id"] == id and usuario_DB[indice]["clave"] == clave:return usuario_DB[indice]
    return "No_Existe"


def registrar_usuario(usuario_DB):
    os.system('cls')
    cabezera()
    espacio()
    marco_menu()
    espacio()
    print("                  " + "\033[4;32;40m" + "Registrando Su Cuenta" + "\033[0m")
    espacio()
    marco_menu()
    
    # Registrar id, clave, nombre, DNI y nivel de Poder
    usuario={"id":"", "clave":"", "nombre":"","DNI":"","nivel":0}
    
    # ingrese id de usuario
    id_existe = True
    while id_existe:
        espacio()
        id = input("Ingrese su id: ")
        if id =="":
            espacio()
            print ("id no puede quedar vacío.")
            continue
        
        # Filtro de id
        for indice in range(len(usuario_DB)):
            if usuario_DB[indice]["id"] == id: 
                espacio()
                print ("Este id ya existe, ingrese otro id, por favor ")
                break
            else:
                if indice == (len(usuario_DB)-1): id_existe = False
            
    
    # ingrese la clave
    intenta = 3
    while True:
        espacio()
        clave = input("Ingrese su clave: ")
        if clave =="":
            espacio()
            print ("La clave no puede quedar vacía.")
            continue
        espacio()
        reclave = input("Ingrese nuevamente su clave: ")
        if clave != reclave:
            espacio() 
            print ("no coincide su clave 💔.")
            intenta -= 1
        else:break
        
        if intenta != 0:
            espacio()
            print (f"Intenta de nuevo, te quedan {intenta} {'💖'*intenta} intentos")
        else: 
            espacio()
            input ("Se agotaron sus intentos 💔\n")
            return False
    
    # ingrese nombre de usuario
    espacio()
    nombre = (input("Ingrese su nombre: ")).capitalize()

    # ingrese DNI de usuario
    DNI_existe = True
    while DNI_existe:
        espacio()
        DNI = input("Ingrese su DNI de 8 Digitos, o Ingrese 0 Para salir de registro: ")
        if DNI == "0": return False
        if DNI =="":
            espacio()
            print ("DNI no puede quedar vacío.")
            continue
        if not(DNI.isdigit()):
            espacio()
            print ("Solo Numero DNI")
            continue
        if not(len(DNI) == 8): 
            espacio()
            print ("DNI ingresado tiene que ser 8 Digitos ")
            continue
        # Filtro de DNI
        for indice in range(len(usuario_DB)):
            if usuario_DB[indice]["DNI"] == DNI: 
                print ("Este DNI ya ha sido registrado, ingrese otro DNI por favor. ")
                break
            else:
                if indice == (len(usuario_DB)-1): DNI_existe = False
        
    # nivel de poder iniciar 0, usuario nuevo
    nivel = 0

    # actualizar direcionario de usuario
    usuario.update({"id":id,"clave":clave,"nombre":nombre,"DNI":DNI,"nivel":nivel})
    
    # Agregar dato de usuario a Base de Datos en lista
    usuario_DB.append(usuario)
    
    # guardar usuario en base de datos
    guardar_DB(archivo_usuario_DB, usuario_DB)
    return True


def listar_usuario(usuario_DB):
    conta = 0
    if (len(usuario_DB)//10)<(len(usuario_DB)/10):
        total = (len(usuario_DB)//10)+1
    else:
        total = (len(usuario_DB)//10)
    i = 0
    while conta < total:
        os.system('cls')
        cabezera()
        espacio()
        print ("*"*85)
        espacio()
        conta +=1
        print("                               " + "\033[1;32;40m" + f"Lista de Usuarios ({conta}/{total})" + "\033[0m")
        espacio()
        print ("*"*85)
        espacio()
        print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
        espacio()
        print(f"{' '*1}|  {'Nª'.center(3)}  | {'id'.center(20)} | {'nombre'.center(20)}| {'DNI'.center(20)} |nivel|")
        espacio()
        print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
        
        while i < (len(usuario_DB)):
            espacio()
            print(f"{' '*1}| {str(i+1).center(3)}.  | {usuario_DB[i]['id'].center(20)} | {usuario_DB[i]['nombre'].center(20)}| {usuario_DB[i]['DNI'].center(20)} |  {usuario_DB[i]['nivel']}  |")
            i += 1
            #Mostrar por 10 linea
            if (i+1)%10 == 1: 
                break
        espacio()
        print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
        print()
        espacio()
        continuar()


def buscar_user(usuario_DB, dato_user):
    for indice in range(len(usuario_DB)):
        if usuario_DB[indice]["id"] == dato_user or usuario_DB[indice]["DNI"] == dato_user or usuario_DB[indice]["nombre"] == dato_user:
            return indice
        else:
            if indice == (len(usuario_DB)-1):
                return "No_Existe"


def modificar_usuario(usuario_DB, usuario): 
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("Modificar Rol de Usuario", usuario)
        espacio()
        marco_menu()
        espacio()
        print("ingresar dato de usuario: "+"\033[1;36;40m" + " id, nombre, DNI " + "\033[0m") 
        espacio()
        dato_user =input("Si desea salir presione '0': ")
        if dato_user == "0": break
        i = buscar_user(usuario_DB, dato_user) # i = indice
        if i != "No_Existe":
            espacio()
            marco_menu()
            espacio()
            print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
            print()
            espacio()
            control = input("Desea cambiar su Rol (" + "\033[1;32;40m" + "S" + "\033[0m" + "/" + "\033[1;31;40m" + "N" + "\033[0m" + "): ")
            if control.upper() == "S":
                if usuario_DB[i] == usuario:
                    print ()
                    espacio()
                    input("No se puede modificar el usuario actual")
                    continue
                espacio()
                rol = input("Cual es el nuevo Rol de Usuario (1. " + "\033[1;32;40m" + "Lector" + "\033[0m" + ", 2. " + "\033[1;31;40m" + "Administrador" + "\033[0m" + ", 0. Salir):")
                if rol == "1":
                    usuario_DB[i]["nivel"] = 1
                    espacio()
                    print ("-"*100)
                    espacio()
                    print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
                    espacio()
                    print ("-"*100)
                    espacio()
                    input("\033[1;33;40m" + f"{usuario_DB[i]['nombre']}" + "\033[0m" + " ahora es " + "\033[1;32;40m" + "Lector" + "\033[0m")
                elif rol == "2":
                    usuario_DB[i]["nivel"] = 2
                    espacio()
                    print ("-"*100)
                    espacio()
                    print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
                    espacio()
                    print ("-"*100)
                    espacio()
                    input("\033[1;33;40m" + f"{usuario_DB[i]['nombre']}" + "\033[0m" + " ahora es " + "\033[1;31;40m" + "Administrador" + "\033[0m")
                elif rol == "0":
                    break
                else:
                    print()
                    espacio()
                    input ("Rol no valido")
                    continue
                guardar_DB(archivo_usuario_DB, usuario_DB)
            else:
                print()
                espacio()
                input ("No se modifico rol de usuario")
                continue
        else:
            print()
            espacio()
            input("Usuario no encontrado, por favor verifique su dato ingresado")


def eliminar_usuario(usuario_DB, usuario):
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("Eliminar el Usuario", usuario)
        espacio()
        marco_menu()
        espacio()
        print("ingresar dato de usuario: "+"\033[1;36;40m" + " id, nombre o DNI " + "\033[0m") 
        espacio()
        dato_user =input("Si desea salir presione '0': ") 
        if dato_user == "0": break
        i = buscar_user(usuario_DB, dato_user) # i = indice
        if i != "No_Existe":
            espacio()
            marco_menu()
            espacio()
            print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
            print ()
            espacio()
            control = input("Desea ELIMINAR este usuario (" + "\033[1;32;40m" + "S" + "\033[0m" + "/" + "\033[1;31;40m" + "N" + "\033[0m" + "): ")
            if control.upper() == "S":
                if usuario_DB[i] == usuario:
                    print ()
                    espacio()
                    input("No se puede eliminar el usuario actual")
                    continue
                control = 0
                for j in range(len(libro_DB)):
                    if libro_DB[j]["Estado"] == usuario_DB[i]["id"]:
                        espacio()
                        input(f"{usuario_DB[i]['nombre']} no puede ser eliminado porque tiene libros prestados")
                        control = 1
                        break
                if control == 1: break
                temp =usuario_DB.pop(i)
                espacio()
                input("\033[1;33;40m" + f"{temp['nombre']}" + "\033[0m" + " ha sido  " + "\033[1;31;40m" + "eliminado" + "\033[0m")
                guardar_DB(archivo_usuario_DB, usuario_DB)
                break
            else:
                print()
                espacio()
                input ("No eliminado ningun usuario")
                break
        else:
            print ()
            espacio()
            input("Usuario no encontrado, por favor verifique el dato ingresado")


def menu_admin_usuario(usuario):
    while True:
            os.system('cls')
            cabezera()
            cabezera_menu("administracion de usuario", usuario)
            espacio()
            print ("1. 🎁 Crear un usuario")
            espacio()
            print ("2. 🥽 Listar todos los usuarios")
            espacio()
            print ("3. 👤 Modificar rol del usuario")
            espacio()
            print ("4. ❌ Eliminar Usuario")
            espacio()
            print ("0. 📕 Salir")
            espacio()
            marco_menu()
            espacio()
            menu_opcion = input ("Elegir un opcion: ")

            # 1. Crear un Usuario
            if menu_opcion == "1":
                exito = registrar_usuario(usuario_DB)
                if exito: 
                    espacio()
                    input("Usuario registrado con exito")
                else: 
                    espacio()
                    input("Usuario no esta registrado ")
                continue
                            
            # 2. listar todos los usuarios
            elif menu_opcion == "2":
                listar_usuario(usuario_DB)
                continue
                            
            # 3. modificar Dato de Usuario
            elif menu_opcion == "3":
                modificar_usuario(usuario_DB, usuario)
                continue
                            
            # 4. Eliminar Usuario
            elif menu_opcion == "4":
                eliminar_usuario(usuario_DB, usuario)
                            
            # 0. Salir
            elif menu_opcion == "0":break
            
            else:
                print()
                espacio()
                input("Ingrese un valor correcto por favor\n")


def registrar_libro(libro_DB):
    os.system('cls')
    cabezera()
    espacio()
    marco_menu()
    espacio()
    print("                 " + "\033[4;32;40m" + "Registrando Libro" + "\033[0m")
    espacio()
    marco_menu()
    print()
    espacio()
    print ("Ingrese los siguientes datos: ")
    espacio()
    print ("\033[1;36;40m" + "Codigo, titulo, autor, año de edicion " + "\033[0m")
    espacio()
    # Registrar id, titulo, autor, año de edicion
    libro = {"id":"", "titulo":"", "autor":"","año de edicion":"","Estado":""}
    # ingrese id de libro
    id_existe = True
    while id_existe:
        print ()
        espacio()
        codigo = input("Ingrese codigo de libro o '0' para cancelar: ")
        if codigo =="":
            espacio()
            print ("código no puede quedar vacío")
            continue
        
        if codigo == "0":
            return False
        
        # Filtro de codigo
        contro = 0
        for lib in libro_DB:
            if lib ["id"] == codigo:
                espacio()
                print ("Este codigo ya existe, ingrese otro codigo, por favor ")
                contro = 1
                break
        if contro == 0: 
            libro["id"] = codigo
            id_existe = False
        else:continue

    # ingrese titulo de libro
    while True:
        espacio()
        libro["titulo"] = (input("ingrese titulo de libro: ")).capitalize()
        if len(libro["titulo"]) > 0:
            break

    # ingrese autor de libro
    while True:
        espacio()
        libro["autor"] = (input("ingrese autor de libro: ")).capitalize()
        if len(libro["autor"]) > 0:
            break
    
    # ingrese año de edicion de libro
    while True:
        espacio()
        libro["año de edicion"] = (input("ingrese año de edicion de libro (4 Digitos): "))
        if len(libro["año de edicion"]) > 0 and len(libro["año de edicion"]) == 4 and libro["año de edicion"].isdigit():
            break
    
    # Agregar dato de libro a Base de Datos en lista
    libro_DB.append(libro)
    
    # guardar usuario en base de datos
    guardar_DB(archivo_libro_DB, libro_DB)
    return True


def marco_libro():

    #                  Nª       id    titulo   autor   Año de Edicion  Reservado
    print(f"{' '*1}+{'-'*7}+{'-'*10}+{'-'*46}+{'-'*27}+{'-'*17}+{'-'*12}+")

def listar_libro(libro_DB):
    # Paginador
    conta = 0
    if (len(libro_DB)//10)<(len(libro_DB)/10):
        total = (len(libro_DB)//10)+1
    else:
        total = (len(libro_DB)//10)
    
    i = 0
    while conta < total:
        os.system('cls')
        cabezera()
        espacio()
        print ("*"*130)
        espacio()
        conta += 1
        print(f"{' '*50} " + "\033[1;32;40m" + f"Lista de Libros ({conta}/{total})" + "\033[0m")
        espacio()
        print ("*"*130)
        espacio()
        marco_libro()
        espacio()
        print(f"{' '*1}|  {'Nª'.center(3)}  | {'Codigo'.center(8)} | {'titulo'.center(45)}| {'autor'.center(25)} | {'Año de Edicion'.center(15)} | {'Reservado'.center(10)} |")
        espacio()
        marco_libro()
        while i < (len(libro_DB)):
            espacio()
            print(f"{' '*1}| {str(i+1).center(3)}.  | {libro_DB[i]['id'].center(8)} | {libro_DB[i]['titulo'].center(45)}| {libro_DB[i]['autor'].center(25)} |  {libro_DB[i]['año de edicion'].center(13)}  |  {libro_DB[i]['Estado'].center(8)}  |")
            i += 1
            #Mostrar por 10 linea
            if (i+1)%10 == 1: 
                break
        espacio()
        marco_libro()
        if conta < total:
            
            espacio()
            continuar()


def buscar_libro(libro_DB, dato_libro):
    for indice in range(len(libro_DB)):
        if dato_libro in libro_DB[indice]["id"].lower() or dato_libro in libro_DB[indice]["titulo"].lower() or dato_libro in libro_DB[indice]["autor"].lower() or dato_libro in libro_DB[indice]["año de edicion"].lower():
            return indice
        else:
            if indice == (len(libro_DB)-1):
                return "No_Existe"


def reservar_libro(libro_DB, usuario):
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("Reserva de libro", usuario)
        espacio()
        print ("Si desea listar los libros disponibles presione ENTER")
        espacio()
        print ("Si desea buscar un libro ingresar dato de libro a buscar")
        espacio()
        dato_libro = (input("Si desea salir presione '0': ") ).lower()
        if dato_libro == "0": break
        # lista de libros buscado
        libro_reservado = []
        # busqueda de libro
        for ilr in range(len(libro_DB)):
            if (dato_libro in libro_DB[ilr]["id"].lower() or dato_libro in libro_DB[ilr]["titulo"].lower() or dato_libro in libro_DB[ilr]["autor"].lower() or dato_libro in libro_DB[ilr]["año de edicion"].lower()) and (libro_DB[ilr]["Estado"] == ""):
                libro_reservado.append(libro_DB[ilr])
        
        if len(libro_reservado) == 0:
            espacio()
            marco_menu()
            espacio()
            input ("No existe libro con el dato ingresado")
            espacio()
            marco_menu()
            continue
        
        if len(libro_reservado) > 1:
            listar_libro(libro_reservado)
            print ()
            espacio()
            input ("Ingrese más palabras del libro para su búsqueda. ")
            espacio()
            marco_menu()
            continue
        
        if len(libro_reservado) == 1:
            listar_libro(libro_reservado)
            print ()
            espacio()
            indice = buscar_libro(libro_DB, dato_libro)
            if usuario["nivel"] == 0:
                    print("Hola " + "\033[1;32;40m" + usuario["nombre"] + "\033[0m" + ", Bienvenido Biblioteca Public.ar, Ud es Usuario Nuevo.")
                    espacio()
                    input("Avisar a Administrador que te asigne un rol para gestion de reserva del libro")
                    continue
                
            control = input("Desea reservar este libro (" + "\033[1;32;40m" + "S" + "\033[0m" + "/" + "\033[1;31;40m" + "N" + "\033[0m" + "): ")
            if control.upper() == "S":
                
                libro_DB[indice]["Estado"] = usuario["id"]
                guardar_DB(archivo_libro_DB, libro_DB)
                if usuario["nivel"] == 2:
                    espacio()
                    input ("El libro " + "\033[1;95;40m" + libro_DB[indice]['titulo'] + "\033[0m" + " ha sido reservado Por " + "\033[4;91;40m" + usuario["nombre"] + "\033[0m")
                else:
                    print ()
                    espacio()
                    input ("El libro " + "\033[1;95;40m" + libro_DB[indice]['titulo'] + "\033[0m" + " ha sido reservado Por " + "\033[4;94;40m" + usuario["nombre"] + "\033[0m")
                continue
            else:
                espacio()
                marco_menu()
                print ()
                espacio()
                input (f"El libro " + "\033[1;95;40m" + libro_DB[indice]['titulo'] + "\033[0m" + "\033[1;31;40m" + " no" + "\033[0m" + " lo reservo. ")
                continue


def devolucion_libro(usuario_DB, libro_DB, usuario) :   
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("Devoluciòn de libro", usuario)
        espacio()
        marco_menu()
        espacio()
        #buscar los libro reservado por usuario
        print ("Ingresar dato de usuario que va a devolver su libro")
        espacio()
        print ("Dato de usuario: "+"\033[1;36;40m" + " id, nombre o DNI " + "\033[0m")
        espacio()
        dato_user =input("Si desea salir presione '0': ") 
        if dato_user == "0": break
        i = buscar_user(usuario_DB, dato_user) # i = indice
        if i != "No_Existe":
            espacio()
            marco_menu()
            espacio()
            print (f"Libros Reservados Por " + "\033[1;31;40m" + usuario_DB[i]['nombre'] + "\033[0m")
            espacio()
            marco_menu()
            # buscar libro reservado por usuario
            control = 0
            for il in range(len(libro_DB)):
                if libro_DB[il]["Estado"] == usuario_DB[i]["id"]:
                    control = 1
                    espacio()
                    print (f"Codigo = {libro_DB[il]['id'].ljust(15)}  titulo = {libro_DB[il]['titulo'].ljust(30)} autor = {libro_DB[il]['autor'].ljust(20)} año de edicion = {libro_DB[il]['año de edicion']}" )
                    espacio()
                    devol = input(f"{usuario_DB[i]['nombre']} Desea devolver este libro (" + "\033[1;32;40m" + "S" + "\033[0m" + "/" + "\033[1;31;40m" + "N" + "\033[0m" + "): ")
                    if devol.upper() == "S":
                        libro_DB[il]["Estado"] = ""
                        
                        guardar_DB(archivo_libro_DB, libro_DB)
                        espacio()
                        marco_menu()
                        espacio()
                        print (f"Libro Devuelto " + "\033[1;95;40m" + f"{libro_DB[il]['titulo']} " + "\033[0m")
                        espacio()
                        marco_menu()
            if control == 0:
                espacio()
                print ("No tiene libros reservados")
                marco_menu()
                espacio()
            espacio()
            continuar()
            break
        else:
            espacio()
            marco_menu()
            espacio()
            print ("No existe el usuario")
            espacio()
            marco_menu()
        espacio()
        continuar()


def eliminar_libro(libro_DB, usuario):
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("Eliminar el Libro", usuario)
        espacio()
        marco_menu()
        espacio()
        print ("Ingresar dato de libro a eliminar")
        espacio()
        print("Dato de libro: " + "\033[1;36;40m" + "Codigo, Titulo o Autor" + "\033[0m")
        espacio()
        dato_libro =input("Si desea salir presione '0': ") 
        if dato_libro == "0": break
        if dato_libro == "":
            espacio()
            input("No puede dejar el campo vacío")
            continue
        il = buscar_libro(libro_DB,dato_libro) # il = indice
        if il != "No_Existe":
            espacio()
            marco_menu()
            espacio()
            print (f"Codigo = {libro_DB[il]['id'].ljust(15)}  Titulo = {libro_DB[il]['titulo'].ljust(30)} Autor = {libro_DB[il]['autor'].ljust(20)}   Año de edicion = {libro_DB[il]['año de edicion']}" )
            print ()
            espacio()
            control = input("Desea ELIMINAR este libro (" + "\033[1;32;40m" + "S" + "\033[0m" + "/" + "\033[1;31;40m" + "N" + "\033[0m" + "): ")
            if control.upper() == "S":
                if libro_DB[il]["Estado"] == "":
                    temp = libro_DB.pop(il)
                    guardar_DB(archivo_libro_DB, libro_DB)
                    espacio()
                    input("\033[1;95;40m" + temp['titulo'] + "\033[0m" + "ha sido " "\033[1;31;40m" + "eliminado" + "\033[0m")
                    break
                else:
                    espacio()
                    input("\033[1;95;40m" + libro_DB[il]['titulo'] + "\033[0m" + " no puede ser eliminado, el libro se encuentra  " + "\033[1;31;40m" + "reservado" + "\033[0m")
                break
            else:
                print ()
                espacio()
                input("No hay Libro eliminado")
                break
        else:
            print ()
            espacio()
            input("Libro no encontrado, por favor verifique el dato ingresado")


def menu_admin_libro(usuario):
    while True:
            os.system('cls')
            cabezera()
            cabezera_menu("administracion de libro", usuario)
            espacio()
            print ("1. 🎁 Registrar un libro")
            espacio()
            print ("2. 👓 Listar todos los libros")
            espacio()
            print ("3. 📅 Reserva de libro")
            espacio()
            print ("4. 📚 Devoluciòn de libro")
            espacio()
            print ("5. ❌ Eliminar de libro")
            espacio()
            print ("0. 📕 Salir")
            espacio()
            marco_menu()
            espacio()
            menu_opcion = input ("Elegir un opcion: ")
            # 1. Crear un Usuario
            if menu_opcion == "1":
                exito = registrar_libro(libro_DB)
                if exito: 
                    espacio()
                    input("Libro registrado con exito")
                else: 
                    espacio()
                    input("Libro no esta registrado ")
                continue
                            
            # 2. listar todos Usuario
            elif menu_opcion == "2":
                listar_libro(libro_DB)
                espacio()
                continuar()
                continue
                            
            # 3. Reservar de libro
            elif menu_opcion == "3":
                reservar_libro(libro_DB, usuario)
                continue
            
            # 4. Devolucion de Libro
            elif menu_opcion == "4":
                devolucion_libro(usuario_DB, libro_DB, usuario)
                continue
                            
            # 5. Eliminar libro
            elif menu_opcion == "5":
                eliminar_libro(libro_DB, usuario)
                            
            # 0. Salir
            elif menu_opcion == "0":break
            else:
                print()
                espacio()
                input("Ingrese un valor correcto por favor\n")


def menu_admin(usuario):
    while True:
        os.system('cls')
        cabezera()
        cabezera_menu("administracion", usuario)
        espacio()
        marco_menu()
        espacio()
        print ("1. 😎 administracion de usuario")
        espacio()
        print ("2. 📚 administracion de libros")
        espacio()
        print ("0. 📕 Salir")
        espacio()
        marco_menu()
        espacio()
        menu_opcion = input ("Elegir un opcion: ")
                        
        # 1. Menu de administracion de usuario 
        if menu_opcion == "1":
            menu_admin_usuario(usuario)

        # 2. administracion de libros
        elif menu_opcion == "2":
            menu_admin_libro(usuario)
                        
        # 0. Salir
        elif menu_opcion == "0":break
        
        else:
            print ()
            espacio()
            input("Ingrese un valor correcto por favor\n")            


def menu_usuario(usuario):
    reservar_libro(libro_DB,usuario)

def logo():
    print("\033[1;36;40m" + """
                                                    ooo                    
                                            ooooooo     ooooooo             
                                          oooo               oooo          
                                        oooo     oooooooooo      oooo       
                                        oo oo ooo          ooo  oo oo       
                                   oooooo   oo    oooooo    oo   oooooo    
                                 oo  oo     oooo          oooo     o  oo    
                                ooooo  oo       oo       oo       o  oo oo 
                                ooooo  oo         oo   oo         o  ooo oo
                                oo  o  oo           ooo           o  oo  oo
                                oo  o  oo            o            o  oo  oo
                                oo  o  oo            o            o  oo  oo
                                oo  o   oo           o           oo  oo  oo
                                oo  o     oo         o         oo    oo  oo
                                oo    ooo   oo       o       o    oo     oo
                                  ooooo   oo   o     0     o   oo   ooooo  
                                    oooooo  oo   o   o   o    oo   oooooo       
                                           oooooooo     oooooooo             
                                                  ooooooo
                                                 
                                          """ + "\033[1;36;40m" + "Biblioteca Pública.ar📚" + "\033[0m" + """                       
                                          """ + "\033[1;36;40m" + "Tu libertd a un click" + "\033[0m" + """
                                                 """ + "\033[0m")


# iniciar programa: Estructura lógica del programa

# cargar base de datos
usuario_DB, libro_DB = cargar_DB(lista_archivos_DB, lista_DB)

os.system('cls')
cabezera()
espacio()
logo()
proceso_100()

while True:
        os.system('cls')
        cabezera()
        print ("""            ----------------------------
            """'\033[1;93;40m' +' ═══>'+"\033[0m" """ Estas en menu inicial"""'\033[1;93;40m' +' ═══╗'+"\033[0m" """
            ----------------------------+ """'\033[1;93;40m' +' V'+"\033[0m" """ 
                                        | Si usted no es usuario, por favor registrese. 
                                        ------------------------------------------------
                                        |  1.📗 Iniciar sesion")                        |
                                        |  2.📒 registrese                              |
                                        |  0.📕 Salir                                   |
                                        -------------------------------------------------  """)
        menu_opcion=input(" "*40 + "Elegir un opcion: ")

        # 1. Iniciar sesion
        if menu_opcion == "1":
            # login usuario return indice de usuario en lista
            usuario = longin(usuario_DB)
            if usuario != "No_Existe":
                # nivel de Poder: 0. usuario nuevo , 1. usuario , 2. administrador
                if usuario["nivel"] == 0:
                    menu_usuario(usuario)
                
                # 1. Menu de usuario
                elif usuario["nivel"] == 1:
                    menu_usuario(usuario)
                
                # 2. Menu de administrador 
                elif usuario["nivel"] == 2:
                    menu_admin(usuario)
            else:
                espacio()
                input("No encontramos el usuario, intente de nuevo") 
        
        # 2. registrese
        elif menu_opcion == "2":
            exito = registrar_usuario(usuario_DB)
            if exito: 
                espacio()
                input("Usuario registrado con exito")
            else: 
                espacio()
                input("Usuario no esta registrado ")
        
        #  0. Salir el Programa
        elif menu_opcion == "0":break
        
        else:
            espacio()
            espacio()
            espacio()
            input("Ingrese un valor correcto por favor\n")
espacio()
print("""

""" + "\033[1;33;40m" + "DRAGONES GROUP🐉" + "\033[0m" + """, agradece su visita a nuestra app 📕📒📗📘
""" + "\033[1;36;40m" + "Luis Altgelt, Gabriela Bentos, Charly Cheng, Ruth Masters" + "\033[0m" + """
""") 

