class Cuenta:
      def __init__  (self, saldo, tipo, fechaCreacion, titular):
        self.saldo = saldo
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion
        self.titular = titular

      def depositar(self,cantidad):
          if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return True
          return False
      
      def retirar(self,cantidad):
          if cantidad >0:
            self.saldo = self.saldo - cantidad
            return True
          return False
      
      def informacion(self):
        print("El saldo de la cuenta es: ", self.saldo,"$")
        print("La cuenta es de tipo: ", self.tipo)
        print("La cuenta se creó el día: ", self.fechaCreacion)
        print("El titular de la cuenta es ", self.titular)
      
