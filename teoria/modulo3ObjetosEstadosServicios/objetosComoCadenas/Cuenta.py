class Cuenta:
      def __init__  (self, saldo, tipo, fechaCreacion):
        self.saldo = saldo
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion
        
      def depositar(self,cantidad):
        if cantidad > 0:
          self.saldo = self.saldo + cantidad
          return True
        else:
          print('La cantidad a depositar debe de ser mayor a cero.')
          return False

      def retirar(self,cantidad):
        if cantidad > self.saldo:
          print('Sin fondos suficientes para el retiro')
          return False
        elif self.saldo >= cantidad > 0:
          self.saldo = self.saldo - cantidad
          return True
        else:
          print('La cantidad a retirar debe de ser mayor a cero.')
          return False

      def informacion(self):
        print("El saldo de la cuenta es: ", self.saldo,"$")
        print("La cuenta es de tipo: ", self.tipo)
        print("La cuenta se creó el día: ", self.fechaCreacion)
   
#Definimos nuestro str para la clase Cuenta
      def __str__(self):
        return f"Saldo::{self.saldo}  ::Tipo::{self.tipo}  ::Fecha de creación::{self.fechaCreacion}"
      
