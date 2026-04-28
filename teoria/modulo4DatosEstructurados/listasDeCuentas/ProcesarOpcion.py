from Cuenta import *

class ProcesadorOpcion:
    def __init__(self, cliente):
        self.cliente = cliente
    
    def procesar(self, opcion):
        if opcion == '1':
            self.mostrarCuentas()
            return True
        
        elif opcion == '2':
            self.depositar()
            return True
        
        elif opcion == '3':
            self.retirar()
            return True
        
        elif opcion == '4':
            self.agregarCuenta()
            return True
        
        elif opcion == '5':
            self.eliminarCuenta()
            return True
        
        elif opcion == '6':
            print("Usted eligió finalizar la sesión, vuelva pronto.")
            return False
        
        else:
            print('Opción no válida, elija entre las opciones 1, 2, 3, 4, 5 o 6.')
            return True
    
    def mostrarCuentas(self):
        print('-----MOSTRAR CUENTAS-----')
        self.cliente.informacionCuentas()
    
    def depositar(self):
        print("-----DEPÓSITO-----")
        # Para depositar debemos escoger primero la cuenta
        cuenta = self.seleccionarCuenta("depositar")
        if cuenta:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            if cuenta.depositar(cantidad):
                print(f"Depósito exitoso, su saldo actual es de: ${cuenta.getSaldo()}")
            else:
                print("No se pudo realizar el depósito")
    
    def retirar(self):
        print('------RETIRO------')
        cuenta = self.seleccionarCuenta("retirar")
        if cuenta:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cuenta.retirar(cantidad):
                print(f"Retiro exitoso, su saldo es de: ${cuenta.getSaldo()}")
            else:
                print("No se pudo realizar el retiro.")
    
    def agregarCuenta(self):
        print('------AGREGAR CUENTA------')
        saldo = float(input("Saldo inicial: "))
        tipo = input("Tipo de cuenta: ")
        fechaCreacion = input("Fecha de creación: ")
        nueva_cuenta = Cuenta(saldo, tipo, fechaCreacion)
        self.cliente.agregarCuenta(nueva_cuenta)
        print("Cuenta agregada exitosamente.")
    
    def eliminarCuenta(self):
        print('------ELIMINAR CUENTA------')
        if len(self.cliente.cuentas) == 0:
            print("No hay cuentas para eliminar.")
            return
        
        self.cliente.informacionCuentas()
        tipo = input("Ingrese el tipo de cuenta a eliminar: ")
        if self.cliente.eliminarCuenta(tipo):
            print("Cuenta eliminada exitosamente.")
        else:
            print("No se encontró la cuenta especificada.")
    
    def seleccionarCuenta(self, movimiento):
        """Permite al usuario elegir una cuenta cuando hay múltiples"""
        if len(self.cliente.cuentas) == 0:
            print(f"No hay cuentas registradas para {movimiento}.")
            return None
        
        if len(self.cliente.cuentas) == 1:
            return self.cliente.cuentas[0]
        
        print(f"Seleccione la cuenta para {movimiento}:")
        self.cliente.informacionCuentas()
        indice = int(input("Número de cuenta: ")) - 1
        
        if 0 <= indice < len(self.cliente.cuentas):
            return self.cliente.cuentas[indice]
        else:
            print("Selección inválida.")
            return None