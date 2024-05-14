import json

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {"productos": []}
    return datos

def guardar_datos(datos, archivo):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

def actualizar_producto(datos):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in datos["productos"]:
        if producto["nombre"] == nombre:
            while True:
                print("¿Qué te gustaría cambiar?")
                print("(1) para modificar el nombre")
                print("(2) para modificar el precio")
                print("(0) para salir")

                opcion = input("Ingrese la opción: ")

                if opcion == "1":
                    producto["nombre"] = input("Ingrese el nuevo nombre: ")
                    print("Se guardó con éxito.")
                elif opcion == "2":
                    producto["precio"] = input("Ingrese el nuevo precio: ")
                    print("Se guardó con éxito.")
                elif opcion == "0":
                    break

def eliminar_producto(datos):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for i in range(len(datos["productos"])):
        if datos["productos"][i]["nombre"] == nombre:
            datos["productos"].pop(i)
            print("Producto eliminado con éxito!")
            return datos
    print("Producto no encontrado.")
    return datos

def menu_productos():
    datos = cargar_datos("productos.json")
    while True:
        print('''
        Menú de Productos:
        (1) Crear producto
        (2) Leer productos
        (3) Actualizar producto
        (4) Eliminar producto
        (5) Devolverse
        ''')
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del nuevo producto: ")
            precio = input("Ingrese el precio del nuevo producto: ")
            nuevo_producto = {"nombre": nombre, "precio": precio}
            datos["productos"].append(nuevo_producto)
            guardar_datos(datos, "productos.json")
            print("Producto creado exitosamente.")
        elif opcion == "2":
            print("Productos:")
            for producto in datos["productos"]:
                print(producto)
        elif opcion == "3":
            actualizar_producto(datos)
            guardar_datos(datos, "productos.json")
        elif opcion == "4":
            datos = eliminar_producto(datos)
            guardar_datos(datos, "productos.json")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_productos()
