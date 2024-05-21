import traceback
import datetime

def manejar_excepcion(excepcion):
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo_excepcion = type(excepcion).__name__
    mensaje_excepcion = str(excepcion)
    
    with open("registro_excepciones.txt", "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora_actual}, Tipo de excepción: {tipo_excepcion}, Mensaje: {mensaje_excepcion}\n")
    
    print("Se ha registrado la excepción en el archivo 'registro_excepciones.txt'.")

try:

    resultado = 1 / 0
except Exception as e:
    manejar_excepcion(e)
   
    print("Ha ocurrido una excepción:", e)
