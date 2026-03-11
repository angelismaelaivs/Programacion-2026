from Cuenta import Cuenta 

class Menu:
  def __init__(self, mensaje, cuenta):
      self.mensajeBienvenida = mensaje
      self.cuenta = cuenta

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
        
        

  def procesaOpcion(self, opcion):
        while True:
            opcion = input('Elija una opción:')
            if opcion == '1':
                print('Usted eligió información de la cuenta.')
                self.cuenta.informacion()
                self.despliegaMenu()
            elif opcion == "2":
                print("Usted eligió hacer un deposito, ingrese la cantidad a depositar:")
                cantidad = float(input())
                self.cuenta.depositar(cantidad)
                print("   Su saldo es de: ", self.cuenta.saldo, "$")
                self.despliegaMenu()
            elif opcion == "3":
                print('Usted eligió hacer un retiro, ingrese la cantidad a retirar:')
                cantidad = float(input())
                self.cuenta.retirar(cantidad)
                print("Su saldo es de: ", self.cuenta.saldo, "$")
                self.despliegaMenu()
            elif opcion == "4":
                print("Usted eligió terminar la sesion, vuelva pronto.")
                break
            else:
                print('Opcion no valida, elija entre las opciones 1, 2, 3 o 4.')
                self.despliegaMenu()
