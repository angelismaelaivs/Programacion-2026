from Cuenta import *

class Menu:

    def __init__(self, mensaje):
        self.mensajeBienvenida = mensaje

    def darBienvenida(self):
        print("Hola bienvenido a la interfaz de tu cuenta Banco Ciencias.")

    def despliegaMenu(self):
            print("------------------------------------------------")
            print ('Selecciona una opción para continuar:')
            print('1. Información de cuenta')
            print('2. Depositar')
            print('3. Retirar')
            print('4. Salir')
            print("------------------------------------------------")
            opcion = input("Elige la opcion deseada:")
            return opcion
            

    def procesaOpcion(self, opcion):
            if opcion == '1':
                print('Usted eligió información de la cuenta.')
                print(self.cuenta1)  #Aquí ocupo el str en Cuenta
                return True
            elif opcion == "2":
                print("Usted eligió hacer un deposito, ingrese la cantidad a depositar:")
                cantidad = float(input())
                if (self.cuenta.depositar(cantidad)):
                    print(f"Deposito exitoso, su saldo es de: {self.cuenta1.saldo}")  #Aquí ocupo el str en Cuenta
                    return True
            elif opcion == "3":
                print('Usted eligió hacer un retiro, ingrese la cantidad a retirar:')
                cantidad = float(input())
                if (self.cuenta.retirar(cantidad)):
                    print(f"Retiro exitoso, su saldo es de: {self.cuenta1.saldo}")  #Aquí ocupo el str en Cuenta
                    return True
            elif opcion == "4":
                print("Usted eligió finalizar la sesion, vuelva pronto.")
                return False
            else:
                print('Opcion no valida, elija entre las opciones 1, 2, 3 o 4.')
                return True
