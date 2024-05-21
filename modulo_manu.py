from modulo_menu_del_menu import menu_usuario
import modulo_productos
from menu_3crud import main
import modulo_reportes
import json
import datetime

def cargar_ventas():
    try:
        with open("ventas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"ventas": []}

def guardar_ventas(ventas):
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo, indent=4)

def migrar_ventas():
    ventas = cargar_ventas()
    for venta in ventas["ventas"]:
        if "fecha_hora" not in venta:
            venta["fecha_hora"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_ventas(ventas)

def mostrar_ventas():
    ventas = cargar_ventas()
    if ventas["ventas"]:
        print("Ventas registradas:")
        for venta in ventas["ventas"]:
            fecha_hora = venta.get("fecha_hora", "Fecha y hora no disponible")
            print(f'Usuario: {venta["usuario"]}, Producto: {venta["producto"]}, Precio: {venta["precio"]}, Fecha y hora: {fecha_hora}')
    else:
        print("No hay ventas registradas.")

def menu_principal():
    
    migrar_ventas()

    while True:
        print('''
              Bienvenido al menú principal de Claro:
              (1) Usuario
              (2) Administrador
              (3) Para salir
              ''')
        pregunta = input("Seleccione una opción: ")
        
        if pregunta == "1":
            print("Bienvenido Usuario")
            from modulo_usuarios import menuusu
            menuusu()
        
        elif pregunta == "2":
            while True:
                print('''
                      Opciones de administrador:
                      (1) Usuario 
                      (2) Productos
                      (3) Servicios
                      (4) Ver ventas
                      (5) Generar reportes
                      (6) Devolverse
                      ''')
                menudelmenu = input("Seleccione una opción: ")

                if menudelmenu == "1":
                    result = menu_usuario()
                    if result == "devolverse":
                        break
                elif menudelmenu == "2":
                    modulo_productos.menu_productos()
                elif menudelmenu == "3":
                    main()
                elif menudelmenu == "4":
                    mostrar_ventas()
                elif menudelmenu == "5":
                    modulo_reportes.menu_reportes()
                elif menudelmenu == "6":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
        elif pregunta == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
