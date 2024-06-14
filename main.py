import os
# variables globales

usuario_DB=[{"id":"admin", "clave":"admin", "nombre":"Charly","apellido":"Cheng","livel":2}]
usuario={"id":"", "clave":"", "nombre":"","apellido":"","livel":0}


# funciones

def longin ():
    os.system('cls')
    global usuario_DB
    print("Longin")
    id=input("Ingrese su id: ")
    clave=input("Ingrese su clave: ")
    for i in range(len(usuario_DB)):
        if usuario_DB[i]["id"]==id and usuario_DB[i]["clave"]==clave:return i
    return "a"


def registro():
    os.system('cls')
    global usuario_DB
    print("Registrando Su Cuenta")
    id=input("Ingrese su id: ")
    clave=input("Ingrese su clave: ")
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    livel=0
    usuario.update({"id":id,"clave":clave,"nombre":nombre,"apellido":apellido,"livel":livel})
    usuario_DB.append(usuario)
    input("Usuario registrado con exito")


def menu_admin(i):
    os.system('cls')
    print("Bienvenido Biblioteca Pública",usuario_DB[i]["nombre"],usuario_DB[i]["apellido"] )
    input("Estamos Trabajando Menu de Administrador")


def menu_usuario(i):
    os.system('cls')
    print("Bienvenido Usuario",usuario_DB[i]["nombre"],usuario_DB[i]["apellido"] )
    input("Estamos Trabajando Menu de Usuario") 


# Inicio Programa

while True:
    while True:
        os.system('cls')
        intento=input("Elegir 1. Iniciar sesion  2. registrese  0. Salir : ")
        if (str.isdigit(intento)):intento=int(intento)
        if (not((intento == 1)or(intento == 2)or(intento == 0))):
            print("\n Ingrese un valor correcto por favor\n")
        if intento==1:
            i=longin()
            if i!="a":
                if usuario_DB[i]["livel"]==0:
                    input("Bienvenido Biblioteca Pública, Ud es Usuario Nuevo, Avisar a Administrador para que le asigne un rol")
                elif usuario_DB[i]["livel"]==1:
                    menu_usuario(i)
                elif usuario_DB[i]["livel"]==2:
                    menu_admin(i)
            else:
                input("No encuentra Su Dato") 
        elif intento==2:
            registro()
            
        elif intento==0:break
    input("Gracia Por Su Visita") 
    break
