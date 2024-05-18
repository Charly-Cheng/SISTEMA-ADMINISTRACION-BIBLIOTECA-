
usuario_DB=[{"id":"admin", "clave":"admin", "nombre":"Charly","apellido":"Cheng","livel":2}]
usuario={"id":"", "clave":"", "nombre":"","apellido":"","livel":0}


def registro():
    id=input("Ingrese su id: ")
    clave=input("Ingrese su clave: ")
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    livel=0
    usuario.update({"id":id,"clave":clave,"nombre":nombre,"apellido":apellido,"livel":livel})
    usuario_DB.append(usuario)
    print("Usuario registrado con exito")


def menu_admin(i):
    print("Bienvenido Biblioteca Pública",usuario_DB[i]["nombre"],usuario_DB[i]["apellido"] )
    print("Estamos Trabajando Menu de Administrador")
    
    
def menu_usuario(i):
    print("Bienvenido Usuario",usuario_DB[i]["nombre"],usuario_DB[i]["apellido"] )
    print("Estamos Trabajando Menu de Usuario")


while True:
    print("1. Iniciar sesion")

    id=input("Ingrese su id: ")
    clave=input("Ingrese su clave: ")

    for i in range(len(usuario_DB)):
        if usuario_DB[i]["id"]==id and usuario_DB[i]["clave"]==clave:
            if usuario_DB[i]["livel"]==0:
                print("Bienvenido Biblioteca Pública, Ud es Usuario Nuevo Avisar a Administrador para que le asigne un rol")
            elif usuario_DB[i]["livel"]==1:
                menu_usuario(i)
            elif usuario_DB[i]["livel"]==2:
                menu_admin(i)
            else:break
        else:
            while True:
                intento=int(input("No encuentra su dato, elegir 1. intente de nuevo o 2. registrese"))
                if intento==1:break
                elif intento==2:
                    registro()
                    break