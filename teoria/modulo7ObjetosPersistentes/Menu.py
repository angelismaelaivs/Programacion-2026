from Cuenta import *
from Cliente import *
from ProcesarOpcion import *

class Menu:

    def __init__(self, mensaje, cliente):
        self.mensajeBienvenida = mensaje
        self.cliente = cliente
        self.procesador = ProcesadorOpcion(cliente)
    
    def darBienvenida(self):
        print("=" * 60)
        print("Hola bienvenido a la interfaz del Banco Ciencias.")
        print("=" * 60)
    
    def desplegarMenu(self):
        while True:
            print("-" * 60)
            print('Selecciona una opción para continuar:')
            print('1. Información de cuentas')
            print('2. Depositar')
            print('3. Retirar')
            print('4. Agregar cuenta')
            print('5. Eliminar cuenta')
            print('6. Salir')
            print("-" * 60)
            
            opcion = input("Elige la opcion deseada: ")
            
            continuar = self.procesador.procesar(opcion)
            
            if not continuar:
                break  