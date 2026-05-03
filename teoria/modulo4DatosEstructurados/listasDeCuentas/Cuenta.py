class Cuenta:
      def __init__  (self, saldo, tipo, fechaCreacion):
        self.__saldo = saldo
        self.__tipo = tipo
        self.__fechaCreacion = fechaCreacion

      def getSaldo(self):
        return self.__saldo
      
      def getTipo(self):
        return self.__tipo
      
      def getFechaCreacion(self):
        return self.__fechaCreacion

      def depositar(self,cantidad):
        if cantidad > 0:
          self.__saldo = self.__saldo + cantidad
          return True                       
        else:
          print('La cantidad a depositar debe de ser mayor a cero.')
          return False                      

      def retirar(self,cantidad):
        if cantidad > self.__saldo:
          print('Sin fondos suficientes para el retiro')
          return False                     
        elif self.__saldo >= cantidad > 0:
          self.__saldo = self.__saldo - cantidad
          return True                       
        else:
          print('La cantidad a retirar debe de ser mayor a cero.')
          return False                     

      def informacion(self):
        print("El saldo de la cuenta es: ", self.__saldo,"$")
        print("La cuenta es de tipo: ", self.__tipo)
        print("La cuenta se creó el día: ", self.__fechaCreacion)
   
      def __str__(self):
        return f"Saldo::{self.__saldo}  ::Tipo::{self.__tipo}  ::Fecha de creación::{self.__fechaCreacion}"
      
