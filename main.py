"""
1. Flujo de programa para unir todos los códigos.
(Interfaz de usuario:
Crear un menú interactivo para que los usuarios (administradores de la biblioteca) puedan interactuar con las diferentes funciones del programa.) similar punto 3. Menú de login.

2. Diseño de interfaz y presentación


3. Menú de login 
    Detectar Usuario de login: en caso:
    Caso a. Si es cuenta administrador, guia a menú de administrador 
    Caso b. Si es cuenta Usuario,  guía a menú de usuario.
    Caso c. Ninguna de los anterio, guía a menú de registra nuevo usuario.


4. Menú de administrador 
    A.Gestion de Libro
        A.a. Agregar un nuevo libro a la biblioteca.
        .b. Mostrar todos los libros disponibles
        A.c. Buscar libros por título, autor o categoría
        A.d. Actualizar la información de un libro.
        A.e. Eliminar un libro de la biblioteca.

    B. Gestión de Usuario
        B.a. Mostrar listo de administrador o usuario 
        B.b Buscar Usuario por nombre o número de usuario o ....
        B.c modificar usuario a administración 
        B.d Eliminar Usuario o Administrador 
        B.e Ver información de un usuario (libros prestados, historial, etc.).
        B.f Actualizar la información de un usuario.

    C. Gestion de Préstamos
        C.a Lista de Reserva o pedidos
        C.b lista de libro prestado
        C.c Registrar el préstamo de un libro a un usuario.
        C.d Registrar la devolución de un libro.
        C.e Mostrar los libros prestados a un usuario específico.


5. Menú de usuario 
    a. Buscar libros por título, autor o categoría
    b. Reserva el libro.

6. Base de datos para guardar todo información.（que datos hay que tener?）
"""





import os

usuario_DB=[{"id":"admin", "clave":"admin", "nombre":"Cheng","DNI":"12345678","livel":2},
            {"id":"123", "clave":"qwe", "nombre":"Charly","DNI":"87654321","livel":1}
            ]
usuario={"id":"", "clave":"", "nombre":"","DNI":"","livel":0}


# funciones

def longin ():
    os.system('cls')
    print("Longin")
    id=input("Ingrese su id: ")
    clave=input("Ingrese su clave: ")
    for i in range(len(usuario_DB)):
        if usuario_DB[i]["id"] == id and usuario_DB[i]["clave"] == clave:return i
    return "No_Existe"


def registro():
    os.system('cls')
    print("Registrando Su Cuenta")
    
    # ingrese id de usuario
    
    id_existe = True
    while id_existe:
        id = input("Ingrese su id: ")
        if id =="":
            print ("id no puede ser vacio.")
            continue
        # Filtro de id
        for i in range(len(usuario_DB)):
            if usuario_DB[i]["id"] == id: 
                print ("Este id ya existe, ingrese otro id, por favor ")
                break
            else:
                if i == (len(usuario_DB)-1): id_existe = False
            
    
    # ingrese la clave
    while True:
        clave = input("Ingrese su clave: ")
        if clave =="":
            print ("La clave no puede ser vacio.")
            continue
        reclave = input("Ingrese nuevamente su clave: ")
        if clave != reclave: print ("no coincide su clave, ingrese de nuevo")
        else:break
    
    nombre = (input("Ingrese su nombre: ")).capitalize()

    # ingreso DNI de usuario
    DNI_existe = True
    while DNI_existe:
        DNI = input("Ingrese su DNI, o Ingrese 0 Para salir de registro: ")
        if DNI == "0": return False
        if DNI =="":
            print ("DNI no puede ser vacio.")
            continue
        if not(DNI.isdigit()):
            print ("Solo Numero DNI")
            continue
        if not(len(DNI) == 8): 
            print ("DNI ingresado no tiene 8 Digitos ")
            continue
        # Filtro de DNI
        for i in range(len(usuario_DB)):
            if usuario_DB[i]["DNI"] == DNI: 
                print ("Este DNI ha sido Registrado, ingrese otro DNI, por favor ")
                break
            else:
                if i == (len(usuario_DB)-1): DNI_existe = False
        
    
    livel=0
    usuario.update({"id":id,"clave":clave,"nombre":nombre,"DNI":DNI,"livel":livel})
    usuario_DB.append(usuario)
    return True


def menu_admin(i):
    os.system('cls')
    print("Bienvenido Biblioteca Públic.ar",usuario_DB[i]["nombre"] )
    input("Estamos Trabajando Menu de Administrador")


def menu_usuario(i):
    os.system('cls')
    print("Bienvenido Usuario",usuario_DB[i]["nombre"])
    input("Estamos Trabajando Menu de Usuario") 


# Inicio Programa


while True:
        os.system('cls')
        intento=input("Elegir 1. Iniciar sesion  2. registrese  0. Salir : ")
        
        # Valida intento 
        if (intento.isdigit()):
            intento=int(intento)  
        if (not((intento == 1)or(intento == 2)or(intento == 0))):
            input("\n Ingrese un valor correcto por favor\n")
            continue
        
        # 1. Iniciar sesion
        if intento == 1:
            i = longin()
            if i!="No_Existe":
                
                # Segun nivel: 0. usuario nuevo , 1. usuario , 2. administrador
                if usuario_DB[i]["livel"] == 0:
                    print(f"Hola {usuario_DB[i]["nombre"]}, Bienvenido Biblioteca Public.ar, Ud es Usuario Nuevo.")
                    input("Avisar a Administrador para que te asigne un rol") 
                elif usuario_DB[i]["livel"] == 1:
                    menu_usuario(i)
                elif usuario_DB[i]["livel"] == 2:
                    menu_admin(i)
            else:
                input("No encuentra Su Dato") 
        
        # 2. registrese
        elif intento == 2:
            exito = registro()
            if exito: input("Usuario registrado con exito")
            else: input("Usuario no esta registrado ")
        
        #  0. Salir el Programa
        elif intento == 0:break
    
input("Gracia Por Su Visita") 

