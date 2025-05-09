import pyfirmata
import time

# en Windows puede ser 'COM3'
# en Linux '/dev/ttyUSB0' o '/dev/ttyACM0'
# En MacOS '/dev/cu.usbserialXXXX'
PUERTO_CONEXION = '/dev/cu.usbserial-A601LNA6'  

def setup():
    print("Configurando Arduino...")

    # Declaración de variables globales para
    # que se puedan usar en la función loop()
    global BOARD, PIN_LED

    BOARD = pyfirmata.Arduino(PUERTO_CONEXION)
    # Esperar que la tarjeta esté operativo
    BOARD.pass_time(0.5) 

    # Configurar el pin del led
    # d:7:o ==> digital pin 7, output
    PIN_LED = BOARD.get_pin('d:7:o') 

    
def loop():
    led_prendido = False
    while True:
        print("Led prendido")
        PIN_LED.write(True)  # Enciende el LED
        time.sleep(1)  #
        print("Led apagado")
        PIN_LED.write(False)
        time.sleep(1) 


setup()
loop()
