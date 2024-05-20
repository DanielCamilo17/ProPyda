import json
import prepago


def cargar_datos():
    try:
        with open("internet_fibra_optica.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"internet_fibra_optica": []}

def guardar_datos(datos):
    with open("internet_fibra_optica.json", "w") as file:
        json.dump(datos, file, indent=4)

def mostrar_planes():
    datos = cargar_datos()
    print("Planes de Internet de fibra óptica:")
    for plan in datos["internet_fibra_optica"]:
        print(plan)

def crear_plan():
    datos = cargar_datos()
    megas = input("Ingrese la cantidad de megas: ")
    precio = input("Ingrese el precio mensual: ")
    nuevo_plan = {"megas": int(megas), "precio_mensual": float(precio)}
    datos["internet_fibra_optica"].append(nuevo_plan)
    guardar_datos(datos)
    print("¡Plan creado exitosamente!")

def actualizar_plan():
    datos = cargar_datos()
    mostrar_planes()
    lista_planes = datos["internet_fibra_optica"]
    
    if not lista_planes:  # Verifica si la lista de planes está vacía
        print("No hay planes disponibles para actualizar.")
        return
    
    indice = int(input("Ingrese el número del plan que desea actualizar: ")) - 1
    
    if indice < 0 or indice >= len(lista_planes):  # Verifica si el índice está fuera del rango
        print("El número de plan ingresado no es válido.")
        return
    
    megas_nuevos = input("Ingrese la nueva cantidad de megas: ")
    precio_nuevo = input("Ingrese el nuevo precio mensual: ")
    
    lista_planes[indice]["megas"] = int(megas_nuevos)
    lista_planes[indice]["precio_mensual"] = float(precio_nuevo)
    
    guardar_datos(datos)
    print("¡Plan actualizado exitosamente!")


def eliminar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea eliminar: ")) - 1
    del datos["internet_fibra_optica"][indice]
    guardar_datos(datos)
    print("¡Plan eliminado exitosamente!")

def gestionar_internet_fibra_optica():
    while True:
        print("Menú de gestión de Internet de fibra óptica:")
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
    while True:

        mostrar_menu()

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            gestionar_internet_fibra_optica()
        elif opcion == "2":
            from crud_Pospago import gestionar_plan_pospago
            gestionar_plan_pospago()

                       
            
        elif opcion == "3":
            from prepago import main3
            main3()

            
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

