from modulo_menu_del_menu import menu_usuario
import modulo_productos
from menu_3crud import main

def menu_principal():
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
            import modulo_usuarios
            from modulo_usuarios import menuusu
            menuusu()
        
        elif pregunta == "2":
            while True:
                print('''
                      Opciones de administrador:
                      (1) Usuario 
                      (2) Productos
                      (3) servicios
                      (4) Devolverse
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
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
        elif pregunta == "3":
            print("Saliendo del programa")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    
