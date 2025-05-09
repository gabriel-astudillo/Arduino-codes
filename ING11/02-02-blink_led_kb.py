import pyfirmata
import time
from pynput import keyboard as kb


KEY_PRESSED = ''
TIME_WAIT = 0.1

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
    global BOARD, PIN_LED

    # Asociar el puerto serie donde está conectado el Arduino
    # Cambia el puerto a uno que funcione para tu computador.
    # Por ejemplo:
    # en Windows puede ser 'COM3'
    # en Linux '/dev/ttyUSB0' o '/dev/ttyACM0'
    # En MacOS '/dev/cu.usbmodemXXXX'
    BOARD = pyfirmata.Arduino('/dev/cu.usbserial-A601LNA6')
    BOARD.pass_time(0.5) # Esperar que la tarjeta esté operativo

    # Configurar el pin del led
    # d:7:o ==> digital pin 7, output
    PIN_LED = BOARD.get_pin('d:7:o') 

    # Iniciar el iterador para leer los pines de entrada y evitar bloqueos en el programa.
    # El iterador lee los pines de entrada y los actualiza en la variable BOARD
    pyfirmata.util.Iterator(BOARD).start() 

    print("Configurando teclado...")
    # Inicia el listener en un hilo separado
    kb.Listener(on_press=on_press, on_release=on_release).start()
    
def loop():
    continuar = True
    while continuar == True:
        if KEY_PRESSED == 'e':
            PIN_LED.write(True)

        elif KEY_PRESSED == 'a':
            PIN_LED.write(False) 
        
        elif KEY_PRESSED == 'q':
            print("Saliendo del programa...")
            # Cerrar la conexión con el Arduino
            BOARD.exit()
            continuar = False
            
        # Espera un tiempo antes de volver a leer el teclado
        time.sleep(TIME_WAIT)  

if __name__ == '__main__':
    setup()
    loop()
