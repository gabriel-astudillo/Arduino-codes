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
    global BOARD, SERVO

    BOARD = pyfirmata.Arduino(PUERTO_CONEXION)
    BOARD.pass_time(0.1) # Wait for the BOARD to be ready

    # Configurar el pin del SERVO
    SERVO = BOARD.get_pin('d:9:s') 

    # Iniciar el iterador para leer los pines de entrada y evitar bloqueos en el programa.
    # El iterador lee los pines de entrada y los actualiza en la variable BOARD
    pyfirmata.util.Iterator(BOARD).start() 

    print("Configurando teadsqclado...")
    # Inicia el listener en un hilo separado
    kb.Listener(on_press=on_press, on_release=on_release).start()


def loop():
    print("Iniciando función loop()...")
    
    servo_stop()

    continuar = True
    while continuar == True:

        if KEY_PRESSED == 'a':
            print("izquierda")
            servo_stop()
            servo_izquierda()

        if KEY_PRESSED == 'd':
            print("derecha")
            servo_stop()
            servo_derecha()

        if KEY_PRESSED == 's':
            print("stop")
            servo_stop()

        if KEY_PRESSED == 'q':
            print("Saliendo del programa...")
            # Detener el servo
            servo_stop()
            # Cerrar la conexión con el Arduino
            BOARD.exit()
            
            continuar = False

        # Esperar un tiempo antes de volver a leer los pines
        time.sleep(TIME_WAIT)

# Funciones para mover el servo
# a la izquierda, derecha o detenerlo
def servo_izquierda():
    SERVO.write(120)
    time.sleep(TIME_WAIT)

def servo_derecha():
    SERVO.write(20)
    time.sleep(TIME_WAIT)

def servo_stop():
    SERVO.write(89)
    time.sleep(TIME_WAIT)



setup()
loop()
