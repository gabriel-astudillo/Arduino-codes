import pyfirmata
import time

PUERTO_CONEXION = '/dev/cu.usbserial-A601LNA6'  
TIME_WAIT = 0.1

def setup():
    print("Configurando Arduino...")

    # Declaración de variables globales para
    # que se puedan usar en la función loop()
    global BOARD, PIN_BOTON

    BOARD = pyfirmata.Arduino(PUERTO_CONEXION)
    # Esperar que la tarjeta esté operativo
    BOARD.pass_time(0.5) 

    # Configurar el pin del led
    # d:7:o ==> digital pin 7, output
    PIN_BOTON = BOARD.get_pin('d:8:i') 

    # Iniciar el iterador para leer los pines de entrada y evitar bloqueos en el programa.
    # El iterador lee los pines de entrada y los actualiza en la variable BOARD
    pyfirmata.util.Iterator(BOARD).start() 

    
def loop():
    while True:
        # Leer el estado del botón
        boton_estado = PIN_BOTON.read()

        if boton_estado == True:
            print("Botón presionado")
        else:
            print("Botón no presionado")
        # Esperar un segundo antes de volver a leer el botón
        time.sleep(TIME_WAIT)


setup()
loop()
