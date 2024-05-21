import json
import datetime
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
    
    usuarios["usuarios"][nombre_usuario] = {"contraseña": contraseña}
    
    guardar_usuarios(usuarios)
    
    print("Usuario creado exitosamente.")

def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if nombre_usuario in usuarios["usuarios"] and usuarios["usuarios"][nombre_usuario]["contraseña"] == contraseña:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
        menu_compras(nombre_usuario)
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def cargar_productos():
    try:
        with open("productos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"productos": []}

def guardar_ventas(ventas):
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo, indent=4)

def cargar_ventas():
    try:
        with open("ventas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"ventas": []}

def comprar_producto(usuario):
    productos = cargar_productos()
    ventas = cargar_ventas()
    
    print("Productos disponibles:")
    for producto in productos["productos"]:
        print(f'Nombre: {producto["nombre"]}, Precio: {producto["precio"]}')
    
    nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
    for producto in productos["productos"]:
        if producto["nombre"] == nombre_producto:
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ventas["ventas"].append({"usuario": usuario, "producto": producto["nombre"], "precio": producto["precio"], "fecha_hora": fecha_hora_actual})
            guardar_ventas(ventas)
            print("Producto comprado exitosamente.")
            return
    
    print("Producto no encontrado.")

def menu_compras(usuario):
    while True:
        print("1. Comprar producto")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            comprar_producto(usuario)
        elif opcion == "2":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

def menuusu():
    while True:
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
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
