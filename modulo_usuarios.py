import json
import modulo_manu

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"usuarios": {}}

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def crear_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    
    if nombre_usuario in usuarios["usuarios"]:
        print("El nombre de usuario ya existe. Intente con otro nombre.")
        return
    
    contraseña = input("Ingrese una contraseña: ")
    
    # Añadimos el nuevo usuario al diccionario
    usuarios["usuarios"][nombre_usuario] = {"contraseña": contraseña}
    
    # Guardamos los usuarios en el archivo JSON
    guardar_usuarios(usuarios)
    
    print("Usuario creado exitosamente.")

def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if nombre_usuario in usuarios["usuarios"] and usuarios["usuarios"][nombre_usuario]["contraseña"] == contraseña:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def menuusu():
    while True:
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input('''
                       
                       Seleccione una opción: 
                       
                    ''')
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            
            print("Saliendo...")
            from modulo_manu import menu_principal
            return menu_principal()
            
        
        else:
            print("Opción no válida.")
            menuusu()

  


