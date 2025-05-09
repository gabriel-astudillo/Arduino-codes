import pyfirmata
import time
from pynput import keyboard as kb


KEY_PRESSED = ''
TIME_WAIT = 0.1

PUERTO_CONEXION = '/dev/cu.usbserial-A601LNA6' 

def on_press(key):
    global KEY_PRESSED
    try:
        if key.char.isalpha():
            KEY_PRESSED = key.char
    except AttributeError:
        pass

def on_release(key):
    global KEY_PRESSED
    try:
        KEY_PRESSED = None
    except AttributeError:
        pass


def setup():
    print("Configurando Arduino...")

    # Declaración de variables globales para
    # que se puedan usar en la función loop()
    global BOARD, PIN_LED, PIN_BOTON

    BOARD = pyfirmata.Arduino(PUERTO_CONEXION)
    BOARD.pass_time(0.5) 

    # Configurar pines
    PIN_LED = BOARD.get_pin('d:7:o') 
    PIN_BOTON = BOARD.get_pin('d:8:i') 

    # Iniciar el iterador para leer los pines de entrada y evitar bloqueos en el programa.
    # El iterador lee los pines de entrada y los actualiza en la variable BOARD
    pyfirmata.util.Iterator(BOARD).start() 

    print("Configurando teclado...")
    # Inicia el listener en un hilo separado
    kb.Listener(on_press=on_press, on_release=on_release).start()
    
def loop():
    led_prendido = False

    continuar = True
    while continuar == True:
        # Leer el estado del botón
        boton_estado = PIN_BOTON.read()
        
        # Esperar un segundo antes de volver a leer el botón
        time.sleep(TIME_WAIT)

        if boton_estado == True:
            led_prendido = not led_prendido
        
        if KEY_PRESSED == 'q':
            print("Saliendo del programa...")
            # Cerrar la conexión con el Arduino
            BOARD.exit()
            continuar = False
        
        PIN_LED.write(led_prendido)
        time.sleep(TIME_WAIT)

setup()
loop()
