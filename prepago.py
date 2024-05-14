import json

def cargar_datos():
    try:
        with open("planes_prepago.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"planes_prepago": []}

def guardar_datos(datos):
    with open("planes_prepago.json", "w") as file:
        json.dump(datos, file, indent=4)

def mostrar_planes():
    datos = cargar_datos()
    print("Planes Prepago:")
    for plan in datos["planes_prepago"]:
        print(plan)

def crear_plan():
    datos = cargar_datos()
    gb = input("Ingrese la cantidad de GB: ")
    precio = input("Ingrese el precio mensual: ")
    nuevo_plan = {"gb": int(gb), "precio_mensual": float(precio)}
    datos["planes_prepago"].append(nuevo_plan)
    guardar_datos(datos)
    print("¡Plan creado exitosamente!")


def actualizar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea actualizar: ")) - 1
    gb_nuevos = input("Ingrese la nueva cantidad de GB: ")
    precio_nuevo = input("Ingrese el nuevo precio mensual: ")
    datos["planes_prepago"][indice]["gb"] = int(gb_nuevos)
    datos["planes_prepago"][indice]["precio_mensual"] = float(precio_nuevo)
    guardar_datos(datos)
    print("¡Plan actualizado exitosamente!")

def eliminar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea eliminar: ")) - 1
    del datos["planes_prepago"][indice]
    guardar_datos(datos)
    print("¡Plan eliminado exitosamente!")

def gestionar_plan_prepago():
    while True:
        print("\nMenú de gestión de Plan prepago:")
        print("1. Mostrar planes")
        print("2. Crear plan")
        print("3. Actualizar plan")
        print("4. Eliminar plan")
        print("5. Volver al menú principal")
        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            mostrar_planes()
        elif opcion == "2":
            crear_plan()
        elif opcion == "3":
            actualizar_plan()
        elif opcion == "4":
            eliminar_plan()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_menu():
    print("Bienvenido al sistema de gestión de servicios de Internet:")
    print("1. Internet de fibra óptica")
    print("2. Plan pospago")
    print("3. Plan prepago")
    print("4. Salir")

def main3():
    gestionar_plan_prepago()



