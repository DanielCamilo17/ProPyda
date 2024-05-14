import json

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()

def actualizar_usuario(datos):
    documento = input("Ingrese el documento del usuario a actualizar: ")
    for usuario in datos["usuarios"]:
        if usuario["documento"] == documento:
            while True:
                print("¿Qué te gustaría cambiar?")
                print("(1) para modificar el nombre")
                print("(2) para modificar la ciudad")
                print("(3) para modificar la edad")
                print("(4) para modificar el documento")
                print("(0) para salir")

                opcion = input("Ingrese la opción: ")

                if opcion == "1":
                    usuario["nombre"] = input("Ingrese el nuevo nombre: ")
                    print("Se guardó con éxito.")
                   
                elif opcion == "2":
                    usuario["ciudad"] = input("Ingrese la nueva ciudad: ")
                    print("Se guardó con éxito.")
                    
                elif opcion == "3":
                    usuario["edad"] = input("Ingrese la nueva edad: ")
                    print("Se guardó con éxito.")
                   
                elif opcion == "4":
                    usuario["documento"] = input("Ingrese el nuevo documento: ")
                    print("Se guardó con éxito.")
                    
                elif opcion == "0":
                    break    


def eliminar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento del usuario a eliminar: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("Usuario eliminado con éxito!")
            return datos
    print("Usuario no encontrado.")
    return datos

         

def menu_usuario():
    datos = cargar_datos("nuevos_datos.json")
    while True:
        opciones = input("""
        opciones de usuario:                 
        (1) crear usuario
        (2) leer usuarios
        (3) actualizar usuarios
        (4) eliminar perfiles de usuarios
        (5) devolverse         
         """)
        if opciones == "1":
           
            nuevo_usuario = {}
            nuevo_usuario["nombre"] = input("Ingrese el nombre del nuevo usuario: ")
            nuevo_usuario["ciudad"] = input("Ingrese la ciudad del nuevo usuario: ")

            while True:
                try:
                    nuevo_usuario["edad"] = int(input("Ingrese la edad del nuevo usuario: "))
                    break
                except ValueError:
                    
                    print("solo se pueden escribir numeros")
                 
            nuevo_usuario["documento"] = input("Ingrese el documento del nuevo usuario: ")
            datos["usuarios"].append(nuevo_usuario)
            guardar_datos(datos, "nuevos_datos.json")
            print("Usuario creado con éxito.")
        elif opciones == "2":
            print("Usuarios:")
            for usuario in datos["usuarios"]:
                print(usuario)  
        elif opciones=="3":
            actualizar_usuario(datos)
        elif opciones=="4":
            datos = eliminar_usuario(datos)
            guardar_datos(datos, "nuevos_datos.json")    
            
            


        elif opciones == "5":
            return "devolverse"