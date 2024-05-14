import json
import prepago

# Función para cargar los datos del archivo JSON
def cargar_datos():
    try:
        with open("internet_fibra_optica.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"internet_fibra_optica": []}

# Función para guardar los datos en el archivo JSON
def guardar_datos(datos):
    with open("internet_fibra_optica.json", "w") as file:
        json.dump(datos, file, indent=4)

# Función para mostrar todos los planes de Internet de fibra óptica
def mostrar_planes():
    datos = cargar_datos()
    print("Planes de Internet de fibra óptica:")
    for plan in datos["internet_fibra_optica"]:
        print(plan)

# Función para crear un nuevo plan de Internet de fibra óptica
def crear_plan():
    datos = cargar_datos()
    megas = input("Ingrese la cantidad de megas: ")
    precio = input("Ingrese el precio mensual: ")
    nuevo_plan = {"megas": int(megas), "precio_mensual": float(precio)}
    datos["internet_fibra_optica"].append(nuevo_plan)
    guardar_datos(datos)
    print("¡Plan creado exitosamente!")

# Función para actualizar un plan de Internet de fibra óptica
def actualizar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea actualizar: ")) - 1
    megas_nuevos = input("Ingrese la nueva cantidad de megas: ")
    precio_nuevo = input("Ingrese el nuevo precio mensual: ")
    datos["internet_fibra_optica"][indice]["megas"] = int(megas_nuevos)
    datos["internet_fibra_optica"][indice]["precio_mensual"] = float(precio_nuevo)
    guardar_datos(datos)
    print("¡Plan actualizado exitosamente!")

# Función para eliminar un plan de Internet de fibra óptica
def eliminar_plan():
    datos = cargar_datos()
    mostrar_planes()
    indice = int(input("Ingrese el número del plan que desea eliminar: ")) - 1
    del datos["internet_fibra_optica"][indice]
    guardar_datos(datos)
    print("¡Plan eliminado exitosamente!")

# Función principal para gestionar los planes de Internet de fibra óptica
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

# Función para mostrar el menú principal
def mostrar_menu():
    print("Bienvenido al sistema de gestión de servicios de Internet:")
    print("1. Internet de fibra óptica")
    print("2. Plan pospago")
    print("3. Plan prepago")
    print("4. Salir")

# Función principal
def main():
    while True:

        mostrar_menu()

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            gestionar_internet_fibra_optica()
        elif opcion == "2":
            gestionar_plan_pospago()
        elif opcion == "3":
            from prepago import main3
            main3()

            
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

