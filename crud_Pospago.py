import json


def cargar_datos():
    try:
        with open("planes_pospago.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"planes_pospago": []}


def guardar_datos(datos):
    with open("planes_pospago.json", "w") as file:
        json.dump(datos, file, indent=4)


def mostrar_planes():
    datos = cargar_datos()
    print("Planes Pospago:")
    for plan in datos["planes_pospago"]:
        print(f"Gigas: {plan['gigas']}, Precio: ${plan['precio']}")


def crear_plan():
    datos = cargar_datos()
    gigas = input("Ingrese la cantidad de gigas: ")
    precio = input("Ingrese el precio mensual: ")
    nuevo_plan = {"gigas": int(gigas), "precio": float(precio)}
    datos["planes_pospago"].append(nuevo_plan)
    guardar_datos(datos)
    print("¡Plan creado exitosamente!")


def actualizar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea actualizar: ")) - 1
    gigas_nuevas = input("Ingrese la nueva cantidad de gigas: ")
    precio_nuevo = input("Ingrese el nuevo precio mensual: ")
    datos["planes_pospago"][indice]["gigas"] = int(gigas_nuevas)
    datos["planes_pospago"][indice]["precio"] = float(precio_nuevo)
    guardar_datos(datos)
    print("¡Plan actualizado exitosamente!")


def eliminar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea eliminar: ")) - 1
    del datos["planes_pospago"][indice]
    guardar_datos(datos)
    print("¡Plan eliminado exitosamente!")


def gestionar_plan_pospago():
    while True:
        print("\nMenú de gestión de Plan pospago:")
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

def main():
    gestionar_plan_pospago()
