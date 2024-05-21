import json

def cargar_productos():
    try:
        with open("productos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"productos": []}

def cargar_ventas():
    try:
        with open("ventas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"ventas": []}

def informe_cantidad_productos():
    productos = cargar_productos()
    print("Cantidad de productos/servicios ofrecidos por la empresa:")
    print(f"Total: {len(productos['productos'])}")
    for producto in productos["productos"]:
        print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}")

def informe_productos_populares():
    ventas = cargar_ventas()
    popularidad = {}
    for venta in ventas["ventas"]:
        producto = venta["producto"]
        if producto in popularidad:
            popularidad[producto] += 1
        else:
            popularidad[producto] = 1
    
    productos_populares = sorted(popularidad.items(), key=lambda x: x[1], reverse=True)
    print("Productos/servicios más populares:")
    for producto, cantidad in productos_populares:
        print(f"Producto: {producto}, Cantidad vendida: {cantidad}")

def informe_usuarios_por_producto():
    ventas = cargar_ventas()
    usuarios_por_producto = {}
    for venta in ventas["ventas"]:
        producto = venta["producto"]
        usuario = venta["usuario"]
        if producto in usuarios_por_producto:
            if usuario in usuarios_por_producto[producto]:
                usuarios_por_producto[producto][usuario] += 1
            else:
                usuarios_por_producto[producto][usuario] = 1
        else:
            usuarios_por_producto[producto] = {usuario: 1}
    
    print("Usuarios que han adquirido cada producto/servicio y la cantidad comprada:")
    for producto, usuarios in usuarios_por_producto.items():
        print(f"Producto: {producto}")
        for usuario, cantidad in usuarios.items():
            print(f"  Usuario: {usuario}, Cantidad: {cantidad}")

def menu_reportes():
    while True:
        print('''
        Menú de Reportes:
        (1) Informe de cantidad de productos/servicios
        (2) Informe de productos/servicios más populares
        (3) Informe de usuarios por producto/servicio
        (4) Devolverse
        ''')
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            informe_cantidad_productos()
        elif opcion == "2":
            informe_productos_populares()
        elif opcion == "3":
            informe_usuarios_por_producto()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
