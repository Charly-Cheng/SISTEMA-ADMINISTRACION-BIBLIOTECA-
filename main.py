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
            {"id": "5", "titulo": "El principito", "año de edicion": "1999", "autor": "Antoine de Saint-Exupéry","Estado":""},
            {"id": "6", "titulo": "El Alquimista", "año de edicion": "1999", "autor": "Paulo Coelho","Estado":""},
            {"id": "7", "titulo": "El Quijote", "año de edicion": "1999", "autor": "Miguel de Cervantes","Estado":""},
            {"id": "8", "titulo": "El Señor de los Anillos", "año de edicion": "1999", "autor": "J.R.R: Tolkien","Estado":""},
            {"id": "9", "titulo": "La Iliada", "año de edicion": "1999", "autor": "Homero","Estado":""},
            {"id": "10", "titulo": "La Odisea", "año de edicion": "1999", "autor": "Homero","Estado":""},
            {"id": "11", "titulo": "La Danza de la Muerte", "año de edicion": "1999", "autor": "George R.R. Martin","Estado":""},

            {"id": "13", "titulo": "El Laberinto de la Soledad", "año de edicion": "1999", "autor": "Gabriel Garcia Marquez","Estado":""},
            ]


# funciones de Menu y operaciones

def guardar_usuario_DB():
    with open("usuario_DB.json", "w") as file:
        json.dump(usuario_DB, file)

def guardar_libro_DB():
    with open("libro_DB.json", "w") as file:
        json.dump(libro_DB, file)

def cargar_usuario_DB():
    with open("usuario_DB.json", "r") as file:
        return json.load(file)

def cargar_libro_DB():
    with open("libro_DB.json", "r") as file:
        return json.load(file)

def continuar ():
    input("Presione ENTER para continuar...")

def longin ():
    os.system('cls')
    print ("-"*35)
    print("            Login")
    print ("-"*35)
    id=input("Ingrese su id: ")
    #clave = input("Ingrese su clave: ")
    clave = getpass.getpass("Ingrese su clave: ")
    
    for indice in range(len(usuario_DB)):
        if usuario_DB[indice]["id"] == id and usuario_DB[indice]["clave"] == clave:return indice
    return "No_Existe"


def registrar_usuario():
    os.system('cls')
    print ("-"*35)
    print("       Registrando Su Cuenta")
    print ("-"*35)
    
    # Registrar id, clave, nombre, DNI y nivel de Poder
    usuario={"id":"", "clave":"", "nombre":"","DNI":"","nivel":0}
    
    # ingrese id de usuario
    id_existe = True
    while id_existe:
        id = input("Ingrese su id: ")
        if id =="":
            print ("id no puede quedar vacío.")
            continue
        
        # Filtro de id
        for indice in range(len(usuario_DB)):
            if usuario_DB[indice]["id"] == id: 
                print ("Este id ya existe, ingrese otro id, por favor ")
                break
            else:
                if indice == (len(usuario_DB)-1): id_existe = False
            
    
    # ingrese la clave
    intenta = 3
    while True:
        clave = input("\nIngrese su clave: ")
        if clave =="":
            print ("La clave no puede quedar vacía.")
            continue
        reclave = input("Ingrese nuevamente su clave: ")
        if clave != reclave: 
            print ("\nno coincide su clave 💔.")
            intenta -= 1
        else:break
        
        if intenta != 0:
            print (f"\nIntenta de nuevo, te quedan {intenta} {'💖'*intenta} intentos")
        else: 
            input ("\nSe agotaron sus intentos 💔\n")
            return False
    
    # ingrese nombre de usuario
    nombre = (input("Ingrese su nombre: ")).capitalize()

    # ingrese DNI de usuario
    DNI_existe = True
    while DNI_existe:
        DNI = input("Ingrese su DNI de 8 Digitos, o Ingrese 0 Para salir de registro: ")
        if DNI == "0": return False
        if DNI =="":
            print ("DNI no puede quedar vacío.")
            continue
        if not(DNI.isdigit()):
            print ("Solo Numero DNI")
            continue
        if not(len(DNI) == 8): 
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
    guardar_usuario_DB()
    return True


def listar_usuario():
    os.system('cls')
    print ("*"*85)
    print("                               Lista de Usuarios")
    print ("*"*85)
    print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
    print(f"{' '*1}|  {'Nª'.center(3)}  | {'id'.center(20)} | {'nombre'.center(20)}| {'DNI'.center(20)} |nivel|")
    print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
    for i in range(len(usuario_DB)):
        print(f"{' '*1}| {str(i+1).center(3)}.  | {usuario_DB[i]['id'].center(20)} | {usuario_DB[i]['nombre'].center(20)}| {usuario_DB[i]['DNI'].center(20)} |  {usuario_DB[i]['nivel']}  |")

        #Mostrar por 25 linea
        if (i+1)%25 == 0: 
            print(f"{' '*1}+-----+----------------------+---------------------+----------------------+-----+")
            input("\nPresione Enter para continuar")
    print(f"{' '*1}+-------+----------------------+---------------------+----------------------+-----+")
    input("\nPresione Enter para continuar")


def buscar_user(dato_user):
    for indice in range(len(usuario_DB)):
        if usuario_DB[indice]["id"] == dato_user or usuario_DB[indice]["DNI"] == dato_user or usuario_DB[indice]["nombre"] == dato_user:
            return indice
        else:
            if indice == (len(usuario_DB)-1):
                return "No_Existe"


def modificar_usuario(indice) :   
    while True:
        os.system('cls')
        print ("-"*35)
        print("Bienvenido Administrador",usuario_DB[indice]["nombre"])
        print("Estas en Zona de Modificar Rol de Usuario")
        print ("-"*35)
        print("ingresar dato de usuario: id, nombre, DNI") 
        dato_user =input("Si desea salir presione '0': ")
        if dato_user == "0": break
        i = buscar_user(dato_user) # i = indice
        if i != "No_Existe":
            print ("-"*35)
            print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
            control = input("\nDesea cambiar su Rol (S/N): ")
            if control.upper() == "S":
                if i == indice:
                    input("\nNo se puede modificar el usuario actual")
                    continue
                rol = input("Cual es el nuevo Rol de Usuario (1. Lector, 2. Administrador, 0. Salir):")
                if rol == "1":
                    usuario_DB[i]["nivel"] = 1
                    print ("-"*100)
                    print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
                    print ("-"*100)
                    input(f"{usuario_DB[i]['nombre']} ahora es Lector")
                elif rol == "2":
                    usuario_DB[i]["nivel"] = 2
                    print ("-"*100)
                    print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
                    print ("-"*100)
                    input(f"{usuario_DB[i]['nombre']} ahora es Administrador")
                elif rol == "0":
                    break
                else:
                    input ("Rol no valido")
                    continue
                guardar_usuario_DB()
        else:
            input("\nUsuario no encontrado, por favor verifique su dato ingresado")


def eliminar_usuario(indice):
    while True:
        os.system('cls')
        print ("-"*35)
        print("Bienvenido Administrador",usuario_DB[indice]["nombre"])
        print("Estas en Zona de Eliminar el Usuario")
        print ("-"*35)
        print("ingresar dato de usuario: id, nombre, DNI") 
        dato_user =input("Si desea salir presione '0': ") 
        if dato_user == "0": break
        i = buscar_user(dato_user) # i = indice
        if i != "No_Existe":
            print ("-"*35)
            print (f"id = {usuario_DB[i]['id'].ljust(20)} nombre = {usuario_DB[i]['nombre'].ljust(20)} DNI = {usuario_DB[i]['DNI'].ljust(20)} nivel = {usuario_DB[i]['nivel']}")
            control = input("\nDesea ELIMINAR este usuario (S/N): ")
            if control.upper() == "S":
                if i == indice:
                    input("\nNo se puede eliminar el usuario actual")
                    continue
                control = 0
                for j in range(len(libro_DB)):
                    if libro_DB[j]["Estado"] == usuario_DB[i]["id"]:
                        input(f"{usuario_DB[i]['nombre']} no puede ser eliminado porque tiene libros prestados")
                        control = 1
                if control == 1: break
                temp =usuario_DB.pop(i)
                input(f"{temp['nombre']} ha sido eliminado")
                guardar_usuario_DB()
                break
            else:
                break
        else:
            input("\nUsuario no encontrado, por favor verifique el dato ingresado")


def menu_admin_usuario(indice):
    while True:
            os.system('cls')
            print ("-"*35)
            print (f"Bienvenido Administrador : {usuario_DB[indice]["nombre"]} ")
            print ("-"*35)
            print ("Estas en Menu de administracion de usuario")
            print ("1. 🎁 Crear un usuario")
            print ("2. 🥽 Listar todos los usuarios")
            print ("3. 👤 Modificar rol del usuario")
            print ("4. ❌ Eliminar Usuario")
            print ("0. 📕 Salir")
            print ("-"*35)
            menu_opcion = input ("Elegir un opcion: ")
                                

            # 1. Crear un Usuario
            if menu_opcion == "1":
                exito = registrar_usuario()
                if exito: input("Usuario registrado con exito")
                else: input("Usuario no esta registrado ")
                continue
                            
            # 2. listar todos los usuarios
            elif menu_opcion == "2":
                listar_usuario()
                continue
                            
            # 3. modificar Dato de Usuario
            elif menu_opcion == "3":
                modificar_usuario(indice)
                continue
                            
            # 4. Eliminar Usuario
            elif menu_opcion == "4":
                eliminar_usuario(indice)
                            
            # 0. Salir
            elif menu_opcion == "0":break
            
            else:input("\n Ingrese un valor correcto por favor\n")


def registrar_libro():
    os.system('cls')
    print ("-"*35)
    print("       Registrando Libro")
    print ("-"*35)
    
    print ("\nIngrese los siguientes datos: ")
    print ("Codigo, titulo, autor, año de edicion ")
    # Registrar id, titulo, autor, año de edicion
    libro = {"id":"", "titulo":"", "autor":"","año de edicion":"","Estado":""}
    # ingrese id de libro
    id_existe = True
    while id_existe:
        codigo = input("\ningrese codigo de libro o '0' para cancelar: ")
        if codigo =="":
            print ("código no puede quedar vacío")
            continue
        
        if codigo == "0":
            return False
        
        # Filtro de codigo
        contro = 0
        for lib in libro_DB:
            if lib ["id"] == codigo:
                print ("Este codigo ya existe, ingrese otro codigo, por favor ")
                contro = 1
                break
        if contro == 0: 
            libro["id"] = codigo
            id_existe = False
        else:continue
        
        
            
    
    # ingrese titulo de libro
    while True:
        libro["titulo"] = (input("ingrese titulo de libro: ")).capitalize()
        if len(libro["titulo"]) > 0:
            break

    # ingrese autor de libro
    while True:
        libro["autor"] = (input("ingrese autor de libro: ")).capitalize()
        if len(libro["autor"]) > 0:
            break
    
    
    # ingrese año de edicion de libro
    while True:
        libro["año de edicion"] = (input("ingrese año de edicion de libro (4 Digitos): "))
        if len(libro["año de edicion"]) > 0 and len(libro["año de edicion"]) == 4 and libro["año de edicion"].isdigit():
            break
    
    # Agregar dato de libro a Base de Datos en lista
    libro_DB.append(libro)
    
    # guardar usuario en base de datos
    guardar_libro_DB()
    return True


def marco_libro():
    #                  Nª       id    titulo   autor   Año de Edicion  Reservado
    print(f"{' '*1}+{'-'*7}+{'-'*10}+{'-'*46}+{'-'*27}+{'-'*17}+{'-'*12}+")

def listar_libro():
    os.system('cls')
    print ("*"*130)
    print(f"{' '*40} Lista de Libros")
    print ("*"*130)
    marco_libro()
    print(f"{' '*1}|  {'Nª'.center(3)}  | {'Codigo'.center(8)} | {'titulo'.center(45)}| {'autor'.center(25)} | {'Año de Edicion'.center(15)} | {'Reservado'.center(10)} |")
    marco_libro()
    for i in range(len(libro_DB)):
        print(f"{' '*1}| {str(i+1).center(3)}.  | {libro_DB[i]['id'].center(8)} | {libro_DB[i]['titulo'].center(45)}| {libro_DB[i]['autor'].center(25)} |  {libro_DB[i]['año de edicion'].center(13)}  |  {libro_DB[i]['Estado'].center(8)}  |")

        #Mostrar por 25 linea
        if (i+1)%25 == 0: 
            marco_libro()
            continuar()
    marco_libro()
    continuar()


def buscar_user(dato_user):
    for indice in range(len(usuario_DB)):
        if usuario_DB[indice]["id"] == dato_user or usuario_DB[indice]["DNI"] == dato_user or usuario_DB[indice]["nombre"] == dato_user:
            return indice
        else:
            if indice == (len(usuario_DB)-1):
                return "No_Existe"

def buscar_libro(dato_libro):
    for indice in range(len(libro_DB)):
        if dato_libro in libro_DB[indice]["id"].lower() or dato_libro in libro_DB[indice]["titulo"].lower() or dato_libro in libro_DB[indice]["autor"].lower() or dato_libro in libro_DB[indice]["año de edicion"].lower():
            return indice
        else:
            if indice == (len(libro_DB)-1):
                return "No_Existe"


def reservar_libro(indice):
    while True:
        os.system('cls')
        print ("-"*35)
        if usuario_DB[indice]["nivel"] == 2:
            print("Bienvenido Administrador",usuario_DB[indice]["nombre"])
        else:
            print("Bienvenido Usuario",usuario_DB[indice]["nombre"])
        print("-"*35)
        print("Estas en Zona de Reserva de libro")
        print ("Si desea listar los libros disponibles presione ENTER")
        print ("Si desea buscar un libro ingresar dato de libro a buscar")
        dato_libro =input("Si desea salir presione '0': ") 
        if dato_libro == "0": break
        libro_reservado = []
        for ilr in range(len(libro_DB)):
            if (dato_libro in libro_DB[ilr]["id"].lower() or dato_libro in libro_DB[ilr]["titulo"].lower() or dato_libro in libro_DB[ilr]["autor"].lower() or dato_libro in libro_DB[ilr]["año de edicion"].lower()) and (libro_DB[ilr]["Estado"] == ""):
                libro_reservado.append(ilr)
            if indice == "No_Existe" :
                break
        
        if len(libro_reservado) == 0:
            print ("-"*35)
            input (f"No existe libro con el dato ingresado")
            print ("-"*35)
            continue
        
        if len(libro_reservado) > 1:
            print ("-"*35)
            print (f"Libros Disponibles")
            print ("-"*35)
            for ilr in range(len(libro_reservado)):
                print (f"Codigo = {libro_DB[libro_reservado[ilr]]['id'].ljust(8)}  Titulo = {libro_DB[libro_reservado[ilr]]['titulo'].ljust(45)} Autor = {libro_DB[libro_reservado[ilr]]['autor'].ljust(25)}   Año de edicion = {libro_DB[libro_reservado[ilr]]['año de edicion']}" )
                if (ilr+1)%25 == 0: continuar()
                
            input ("\nIngrese más palabras del libro para su búsqueda. ")
            print ("-"*35)
            continue
        
        if len(libro_reservado) == 1:
            print ("-"*35)
            print (f"Libro Disponible")
            print ("-"*35)
            print (f"Codigo = {libro_DB[libro_reservado[0]]['id'].ljust(15)}  Titulo = {libro_DB[libro_reservado[0]]['titulo'].ljust(30)} Autor = {libro_DB[libro_reservado[0]]['autor'].ljust(20)}   Año de edicion = {libro_DB[libro_reservado[0]]['año de edicion']}" )
            control = input("\nDesea reservar este libro (S/N): ")
            if control.upper() == "S":
                libro_DB[libro_reservado[0]]["Estado"] = usuario_DB[indice]["id"]
                guardar_libro_DB()
                input (f"\nEl libro {libro_DB[libro_reservado[0]]['titulo']} ha sido reservado Por {usuario_DB[indice]["nombre"]}  ")
                print ("-"*35)
                print ("-"*35)
                continue
            else:
                print ("-"*35)
                input (f"\nEl libro {libro_DB[libro_reservado[0]]['titulo']} no esta Reservado. ")
                print ("-"*35)
                continue




def devolucion_libro(indice) :   
    
    while True:
        os.system('cls')
        print ("-"*35)
        print("Bienvenido Administrador",usuario_DB[indice]["nombre"])
        print("Estas en Zona de Devoluciòn de libro")
        print ("-"*35)
        #buscar los libro reservado por usuario
        print ("Ingresar dato de usuario que va a devolver su libro")
        print ("Dato de usuario: id, nombre o DNI ")
        dato_user =input("Si desea salir presione '0': ") 
        if dato_user == "0": break
        i = buscar_user(dato_user) # i = indice
        if i != "No_Existe":
            print ("-"*35)
            print (f"Libros Reservados Por {usuario_DB[i]['nombre']}")
            print ("-"*35)
            
            for il in range(len(libro_DB)):
                if libro_DB[il]["Estado"] == usuario_DB[i]["id"]:
                    print (f"Codigo = {libro_DB[il]['id'].ljust(15)}  titulo = {libro_DB[il]['titulo'].ljust(30)} autor = {libro_DB[il]['autor'].ljust(20)} año de edicion = {libro_DB[i]['año de edicion']}" )
                    devol = input(f"{usuario_DB[i]['nombre']} Desea devolver este libro (S/N): ")
                    if devol.upper() == "S":
                        libro_DB[il]["Estado"] = ""
                        
                        guardar_libro_DB()
                        print ("-"*35)
                        print (f"Libro Devuelto {libro_DB[il]['titulo']}")
                        print ("-"*35)
            continuar()
            break
        else:
            print ("-"*35)
            print ("No existe el usuario")
            print ("-"*35)
            
        continuar()
            


def eliminar_libro(indice):
    while True:
        os.system('cls')
        print ("-"*35)
        print("Bienvenido Administrador",usuario_DB[indice]["nombre"])
        print("Estas en Zona de Eliminar el Libro")
        print ("-"*35)
        print ("Ingresar dato de libro a eliminar")
        print("Dato de libro: Codigo, Titulo o Autor ")
        dato_libro =input("Si desea salir presione '0': ") 
        if dato_libro == "0": break
        il = buscar_libro(dato_libro) # il = indice
        if il != "No_Existe":
            print ("-"*35)
            print (f"Codigo = {libro_DB[il]['id'].ljust(15)}  Titulo = {libro_DB[il]['titulo'].ljust(30)} Autor = {libro_DB[il]['autor'].ljust(20)}   Año de edicion = {libro_DB[il]['año de edicion']}" )
            control = input("\nDesea ELIMINAR este libro (S/N): ")
            if control.upper() == "S":
                if libro_DB[il]["Estado"] == "":
                    temp = libro_DB.pop(il)
                    guardar_libro_DB()
                    input(f"Libro {temp['titulo']} eliminado")
                    break
                else:
                    input(f"Libro {libro_DB[il]['titulo']} no puede ser eliminado, el libro se encuentra reservado")
                break
            else:
                input("\nNo hay Libro  eliminado")
                break
        else:
            input("\nLibro no encontrado, por favor verifique el dato ingresado")






def menu_admin_libro(indice):
    global usuario_DB
    while True:
            os.system('cls')
            print ("-"*35)
            print (f"Bienvenido Administrador : {usuario_DB[indice]["nombre"]} ")
            print ("-"*35)
            print ("Estas en Menu de administracion de libro")
            print ("1. 🎁 Registrar un libro")
            print ("2. 👓 Listar todos los libros")
            print ("3. 📅 Reserva de libro")
            print ("4. 📚 Devoluciòn de libro")
            print ("5. ❌ Eliminar de libro")
            print ("0. 📕 Salir")
            print ("-"*35)
            menu_opcion = input ("Elegir un opcion: ")
                                

            # 1. Crear un Usuario
            if menu_opcion == "1":
                exito = registrar_libro()
                if exito: input("Libro registrado con exito")
                else: input("Libro no esta registrado ")
                continue
                            
            # 2. listar todos Usuario
            elif menu_opcion == "2":
                listar_libro()
                continue
                            
            # 3. Reservar de libro
            elif menu_opcion == "3":
                reservar_libro(indice)
                continue
            
            # 4. Devolucion de Libro
            elif menu_opcion == "4":
                devolucion_libro(indice)
                continue
                            
            # 5. Eliminar libro
            elif menu_opcion == "5":
                eliminar_libro(indice)
                            
            # 0. Salir
            elif menu_opcion == "0":break
            
            else:input("\n Ingrese un valor correcto por favor\n")




def menu_admin(indice):
    while True:
        os.system('cls')
        print ("-"*35)
        print(f"Bienvenido Administrador : {usuario_DB[indice]["nombre"]}  ")
        print ("-"*35)
        print ("1. 😎 administracion de usuario")
        print ("2. 📚 administracion de libros")
        print ("0. 📕 Salir")
        print ("-"*35)
        menu_opcion = input ("Elegir un opcion: ")
                        
        # 1. Menu de administracion de usuario 
        if menu_opcion == "1":
            menu_admin_usuario(indice)

        # 2. administracion de libros
        elif menu_opcion == "2":
            menu_admin_libro(indice)
                        
        # 0. Salir
        elif menu_opcion == "0":break
        
        else:input("\n Ingrese un valor correcto por favor\n")            


def menu_usuario(indice):

        reservar_libro(indice)

def logo():
    print ("""

                                                  ,]/@@@@@@@@@@@@@@@@@@@@@@@@]]                    
                                             ,]@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\`              
                                         ]@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@]          
                                     ,/@@@@@@@@@@@@@@/[`                   ,[\@@@@@@@@@@@@@@\`      
                                   /@@@@@@@@@@@/[                                 [\@@@@@@@@@@@\`   
                                ]@@@@@@@@@@/`                                         ,\@@@@@@@@@@\                                                
                        ]@@@\`/@@@@@@@@@[  						[@@@@@@@@@\,/@@@]                                        
                      =@@@@@@@@@@@@@@/                   ]]/@@@@@@@@@@@\]]                   \@@@@@@@@@@@@@@^                                      
                      =@@@@@@@@@@@@`o              ]@@@@@@@@@@@@@@@@@@@@@@@@@@@]`              ,@@@@@@@@@@@@^                                      
                      =@@@@@@@@@@o  o         ,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\`            ,@@@@@@@@@@^                                      
                      =@@@@@@@@@@@@oo]]]]]]]/@@@@@@@@@@O]]]]]]]]]]]]]]]]]]]O@@@@@@@@@@@]]]]]]]]]/@@@@@@@@@@@^                                      
                      =@@@@@@oO@@@@@@ooooO@@@@@@@@OoooooooooooooooooooooooooooooO@@@@@@@@Ooooo@@@@@@@oO@@@@@^                                      
             /@@@@\   =@@@@@@oooO@@@@@@@@@@@@@@ooooooooooooooooooooooooooooooooooooo@@@@@@@@@@@@@@@oooO@@@@@^   /@@@@\                             
           ,@@@@@@@@@@/@@@@@@oooooO@@@@@@@@@OoooooooooooooooooooooooooooooooooooooooooO@@@@@@@@@@oooooO@@@@@\/@@@@@@@@@`                           
           =@@@@@@@@@@@@@@@@@oooooooO@@@@@@oooooooooooooooO@@@@@@@@@@@@@Oooooooooooooooo@@@@@@OoooooooO@@@@@@@@@@@@@@@@^                           
           =@@@@@@@@@@@@@@@@@oooooooooO@@@@@@ooooooooo@@@@@@@@@@@@@@@@@@@@@@@ooooooooo@@@@@@OoooooooooO@@@@@@@@@@@@@@@@^                           
           =@@@@@@oo@@@@@@@@@oooooooooooO@@@@@@oooo@@@@@@@@@@@@OOOOO@@@@@@@@@@@@oooo@@@@@@OoooooooooooO@@@@@@@@oo@@@@@@^                           
           =@@@@@@oooooO@@@@@oooooooooooooO@@@@@@@@@@@@@@ooooooooooooooooo@@@@@@@@@@@@@@OoooooooooooooO@@@@Oooooo@@@@@@^                           
           =@@@@@@oooooO@@@@@oooooooooooooooO@@@@@@@@@ooooooooooooooooooooooo@@@@@@@@@Oooooooooooooooo@@@@@Oooooo@@@@@@^                           
           =@@@@@@oooooO@@@@@oooooooooooooooooO@@@@@@ooooooooooooooooooooooooo@@@@@@Oooooooooooooooooo@@@@@Oooooo@@@@@@^                           
  ,/@@@@]  =@@@@@@oooooO@@@@@oooooooooooooooooooO@@@@@@ooooooooooooooooooooo@@@@@@Oooooooooooooooooooo@@@@@Oooooo@@@@@@^  ]@@@@\`                  
 =@@@@@@@@@@@@@@@@oooooO@@@@@oooooooooooooooooooooO@@@@@@oooO@@@@@@@@@Oooo@@@@@@Oooooooooooooooooooooo@@@@@Oooooo@@@@@@@@@@@@@@@@^                 
 =@@@@@@@@@@@@@@@@oooooO@@@@@oooooooooooooooooooooooO@@@@@@@@@@@@@@@@@@@@@@@@@Oooooooooooooooooooooooo@@@@@Oooooo@@@@@@@@@@@@@@@@@                 
 =@@@@@@@@@@@@@@@@oooooO@@@@@oooooooooooooooooooooooooO@@@@@@@@OOooO@@@@@@@@Oooooooooooooooooooooooooo@@@@@Oooooo@@@@@@@@@@@@@@@@@                 
 =@@@@@OoooO@@@@@@oooooO@@@@@oooooooooooooooooooooooooooO@@@@@@ooooo@@@@@@Oooooooooooooooooooooooooooo@@@@@Oooooo@@@@@@@oooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@oooooooooooooooooooooooooooooO@@@@@@o@@@@@@Oooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@oooooooooooooooooooooooooooooooO@@@@@@@@@Oooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@oooooooooooooooooooooooooooooooooO@@@@@Oooooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@oooooooooooooooooooooooooooooooooo@@@@@oooooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@ooooooooooooooooooooooooooooooooooO@@@@oooooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@ooooooooooooooooooooooooooooooooooO@@@@oooooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@ooooo@@@@@oooooO@@@@@ooooooooooooooooooooooooooooooooooO@@@@oooooooooooooooooooooooooooooooooo@@@@@Oooooo@@@@@oooooO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@ooOOOOOoooOOOOOooooOOOooOOOOooOOoOO@@@OooOOOOOOOOOOooooOOOOOoooOOOOOoOOoo@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@OoOOOoOOOOoOOOoOOOOOOOooOOooOOOooOO@@@OOOooOOOOOOooOOOOoOOooOOOOoOOOoOOOoO@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@OoOOOoOOOOOOOOOOOoooOOooOOooOOOOoOO@@@OOOooOOOOOOooOOOOOOOooOOOOoOOOoOOOo@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOO@@@@@@@OOOoOOOOoOOOoOOOooOOooOOOoOOOOoOO@@@OOOoOOOOoOOOoOOOooOOOoOOOoOOOOoOO@@@@@@@OOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOOOO@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@OOOOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOOOOOO@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@OOOOOOOOOO@@@@@OOOOOO@@@@@@                 
 =@@@@@@OOOOO@@@@@OOOOOOOOOOOOO@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@OOOOOOOOOOOOO@@@@@OOOOO@@@@@@@                 
 =@@@@@@OOOOO@@@@@@@OOOOOOOOOOOOO@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOO@@OOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@OOOOOOOOOOOOO@@@@@@@OOOOO@@@@@@@                 
 =@@@@@@OOOOOO@@@@@@@@@@OOOOOOOOOOO@@@@@@OOOOOOOOOOOOOOOOOOOOOOOO@@OOOOOOOOOOOOOOOOOOOOOOO@@@@@@OOOOOOOOOOO@@@@@@@@@@OOOOOO@@@@@@@                 
 =@@@@@@OOOOOOOOOO@@@@@@@@@OOOOOOOOOOO@@@@@OOOOOOOOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOOOOOOOOO@@@@@OOOOOOOOOOO@@@@@@@@@OOOOOOOOOO@@@@@@@                 
 =@@@@@@@@OOOOOOOOOOOO@@@@@@@@@OOOOOOOOO@@@@@OOOOOOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOOOOOOO@@@@@OOOOOOOOO@@@@@@@@@OOOOOOOOOOOO@@@@@@@@@                 
 =@@@@@@@@@@@@@@OOOOOOOOOOO@@@@@@@OOOOOOOOO@@@@OOOOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOOOOO@@@@OOOOOOOOO@@@@@@@OOOOOOOOOOOO@@@@@@@@@@@@@@                 
  [@@@@@@@@@@@@@@@@@@OOOOOOOOOO@@@@@@@OOOOOOO@@@@OOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOOO@@@@OOOOOOOO@@@@@@OOOOOOOOOO@@@@@@@@@@@@@@@@@@[`                 
       ,\@@@@@@@@@@@@@@@@@@OOOOOOOO@@@@@@OOOOOOO@@@OOOOOOOOOOOOOO@OOOOOOOOOOOOOO@@@OOOOOOO@@@@@@OOOOOOOOO@@@@@@@@@@@@@@@@@/[                       
             [\@@@@@@@@@@@@@@@@@OOOOOOO@@@@@@OOOOO@@@OOOOOOOOOOOO@OOOOOOOOOOOO@@@OOOOOO@@@@@OOOOOOO@@@@@@@@@@@@@@@@@@[`                            
                  ,[@@@@@@@@@@@@@@@@@@OOOOO@@@@@OOOOO@@OOOOOOOOOO@OOOOOOOOOO@@@OOOO@@@@@OOOOO@@@@@@@@@@@@@@@@@@/`                                  
                        [\@@@@@@@@@@@@@@@@@OOOOO@@@@OOO@@OOOOOOOOOOOOOOOOO@@OOOO@@@@OOOO@@@@@@@@@@@@@@@@@@[                                        
                             ,[@@@@@@@@@@@@@@@@@@OOO@@@OO@@OOOOOOOOOOOOO@@OO@@@OOO@@@@@@@@@@@@@@@@@@/`                                             
                                   [\@@@@@@@@@@@@@@@@@OO@@@O@OOOOOOOOO@OO@@OO@@@@@@@@@@@@@@@@@@[    
                                        ,[@@@@@@@@@@@@@@@@@@@@@OOOOO@@@@@@@@@@@@@@@@@@@@@/`         
                                              [\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/[               
                                                   ,[@@@@@@@@@@@@@@@@@@@@@@@@@[`                    
                                                          [\@@@@@@@@@@@@@/[                          
                                                               ,[@@@[`                               

""")      
"""      
      
      
      
      
      
      
      
      
      
                                    						                       =@@@@@@@             @@@@@@@^  /@@@@@@`                         
                                    						                       =@@@@@@@             @@@@@@@^ ,@@@@@@@@                         
                                   						                           =@@@@@@@             @@@@@@@^  \@@@@@@^                         
                                           ]]]]]]` ]/@@@\]     ,]]]]]]]   ]]]]]]]` =@@@@@@@,]@@@@]`     @@@@@@@^  ,]]]]]]`      ,]@@@@@\]                 ,]]/@@@@@@]     ,]]]]]]` ]@@@           
                                           @@@@@@@@@@@@@@@@\   =@@@@@@@  =@@@@@@@^ =@@@@@@@@@@@@@@@@^   @@@@@@@^  @@@@@@@^    /@@@@@@@@@@@             ,@@@@@@@@@@@@@@@   =@@@@@@@@@@@@           
                                           @@@@@@@@@@@@@@@@@^  =@@@@@@@  =@@@@@@@^ =@@@@@@@@@@@@@@@@@`  @@@@@@@^  @@@@@@@^   @@@@@@@@@@@@^              @@@@@@@@@@@@@@@^  =@@@@@@@@@@@@           
                                           @@@@@@@@[[@@@@@@@@  =@@@@@@@  =@@@@@@@^ =@@@@@@@/[\@@@@@@@^  @@@@@@@^  @@@@@@@^  /@@@@@@@/[@@@^              =@@@@@@@@@@@@@@/  =@@@@@@@@@@@@           
                                           @@@@@@@^  =@@@@@@@` =@@@@@@@  =@@@@@@@^ =@@@@@@@   @@@@@@@\  @@@@@@@^  @@@@@@@^  @@@@@@@^                            =@@@@@@^  =@@@@@@@^               
                                           @@@@@@@^  =@@@@@@@^ =@@@@@@@  =@@@@@@@^ =@@@@@@@   @@@@@@@@  @@@@@@@^  @@@@@@@^ =@@@@@@@^                     ]@@@@@@@@@@@@@^  =@@@@@@@                
                                           @@@@@@@^  =@@@@@@@^ =@@@@@@@  =@@@@@@@^ =@@@@@@@   @@@@@@@/  @@@@@@@^  @@@@@@@^ =@@@@@@@^                   ,@@@@@@@@@@@@@@@^  =@@@@@@@                
                                           @@@@@@@^  =@@@@@@@  =@@@@@@@  =@@@@@@@^ =@@@@@@@   @@@@@@@^  @@@@@@@^  @@@@@@@^  @@@@@@@^                   @@@@@@@  =@@@@@@^  =@@@@@@@                
                                           @@@@@@@@@@@@@@@@@/  =@@@@@@@@@@@@@@@@@^ =@@@@@@@@@@@@@@@@@`  @@@@@@@@^ @@@@@@@^  =@@@@@@@@@@@@    /@@@@@@`  @@@@@@@\]/@@@@@@@@`=@@@@@@@                
                                           @@@@@@@@@@@@@@@@@   =@@@@@@@@@@@@@@@@@^ =@@@@@@@@@@@@@@@@^   @@@@@@@@^ @@@@@@@^   \@@@@@@@@@@@`   @@@@@@@@  =@@@@@@@@@@@@@@@@@ =@@@@@@@                
                                           @@@@@@@@@@@@@@@/     ,@@@@@@@@`@@@@@@@^ =@@@@@@\@@@@@@@@`     \@@@@@@^ @@@@@@@^     \@@@@@@@@@^   =@@@@@@`   ,@@@@@@@/ @@@@@@@ =@@@@@@@                
                                           @@@@@@@@                                                 
                                           @@@@@@@@                                                 
                                           @@@@@@@@                                                 
      
"""



# iniciar programa: Estructura lógica del programa

# inicio base de datos
if os.path.exists("pusuario_DB.json"):usuario_DB = cargar_usuario_DB()
else: guardar_usuario_DB() 
    
if os.path.exists("libro_DB.json"):libro_DB = cargar_libro_DB()
else: guardar_libro_DB()

while True:
        os.system('cls')
        #logo()
        print("Sistema de Administración de una Biblioteca Pública📚")
        print("Te damos la bienvenida 🤝 a Public.ar") 
        print("Si usted no es usuario, por favor registrese.")
        
        print ("-"*35)
        print ("1.📗 Iniciar sesion")
        print ("2.📒 registrese")
        print ("0.📕 Salir")
        print ("-"*35)
        menu_opcion=input("Elegir un opcion: ")
        
        
        # 1. Iniciar sesion
        if menu_opcion == "1":
            # login usuario return indice de usuario en lista
            indice = longin()
            if indice != "No_Existe":
                # nivel de Poder: 0. usuario nuevo , 1. usuario , 2. administrador
                if usuario_DB[indice]["nivel"] == 0:
                    print(f"Hola {usuario_DB[indice]["nombre"]}, Bienvenido Biblioteca Public.ar, Ud es Usuario Nuevo.")
                    input("Avisar a Administrador para que te asigne un rol")
                
                # 1. Menu de usuario
                elif usuario_DB[indice]["nivel"] == 1:
                    menu_usuario(indice)
                
                # 2. Menu de administrador 
                elif usuario_DB[indice]["nivel"] == 2:
                    menu_admin(indice)
            else:
                input("No encontramos el usuario, intente de nuevo") 
        
        # 2. registrese
        elif menu_opcion == "2":
            exito = registrar_usuario()
            if exito: input("Usuario registrado con exito")
            else: input("Usuario no esta registrado ")
        
        #  0. Salir el Programa
        elif menu_opcion == "0":break
        
        else:input("\n Ingrese un valor correcto por favor\n")
    
print("""

DRAGONES GROUP, agradece su visita a nuestra app 📕📒📗📘
Luis Altgelt, Gabriela Bentos, Charly Cheng, Ruth Masters
""") 

