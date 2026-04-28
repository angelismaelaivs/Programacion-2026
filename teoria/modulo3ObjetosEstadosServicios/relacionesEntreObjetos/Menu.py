from Cuenta import *

class Menu:

    def __init__(self, mensaje, cuenta):
        self.mensajeBienvenida = mensaje
        self.cuenta = cuenta

    def darBienvenida(self):
        print("=" * 60)
        print("Hola bienvenido a la interfaz de tu cuenta Banco Ciencias.")
        print("=" * 60)

    def despliegaMenu(self):
            print("-" * 60)
            print ('Selecciona una opción para continuar:')
            print('1. Información de cuenta')
            print('2. Depositar')
            print('3. Retirar')
            print('4. Salir')
            print("-" * 60)
            opcion = input("Elige la opcion deseada:")
            return opcion
            

    def procesaOpcion(self, opcion):

            if opcion == '1':
                print('-----INFORMACIÓN DE LA CUENTA-----')
                print(self.cuenta)  #Aquí ocupo el str en Cuenta
                return True
            
            elif opcion == "2":
                print("-----DEPÓSITO-----")
                cantidad = float(input("Ingrese la cantidad a depostitar:"))
                if (self.cuenta.depositar(cantidad)):
                    print(f"Deposito exitoso, su saldo actual es de: {self.cuenta.saldo}")  #Aquí ocupo el str en Cuenta
                else:
                    print("No se pudo realizar el deposito")
                    
                return True
                
            elif opcion == "3":
                print('------RETIRO------')
                cantidad = float(input("Ingrese la cantidad a retirar:"))
                if (self.cuenta.retirar(cantidad)):
                    print(f"Retiro exitoso, su saldo es de: {self.cuenta.saldo}")  #Aquí ocupo el str en Cuenta
                else:
                    print("No se pudo realizar el retiro.")
                return True
                
            elif opcion == "4":
                print("Usted eligió finalizar la sesion, vuelva pronto.")
                return False
            else:
                print('Opcion no valida, elija entre las opciones 1, 2, 3 o 4.')
                return True
            
                 
