from modulo_menu_del_menu import menu_usuario

def menu_principal():
    while True:
        print( '''
              Bienvendio  al menu principal de Claro :''')
        pregunta = input('''
        (1) usuario
        (2) administrador                
        (3) para salir ''')
         
        if pregunta == "1":
            print("bienvenido usuario")
            break
        elif pregunta == "2":
            while True:
                menudelmenu = input('''
                 
            opciones de administrador:
            (1) usuario 
            (2) productos
            (3) planes
            (4) devolverse ''')
                if menudelmenu == "1":
                 
                 result = menu_usuario()
                 if result == "devolverse":
                    continue
                elif menudelmenu=="4":
                   break
                   menu_principal()
                    
                    
                    
                     
        elif pregunta == "3":
            print("Saliendo del programa")
            break
        else:
            print("dato no válido, intente nuevamente")

menu_principal()
