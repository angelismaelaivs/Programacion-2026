class Cuenta:
  def __init__  (self, saldo, tipo, fechaCreacion):
    self.saldo = saldo
    self.tipo = tipo
    self.fechaCreacion = fechaCreacion

  def depositar(self,cantidad):
    self.saldo = self.saldo + cantidad

  def retirar(self,cantidad):
    self.saldo = self.saldo - cantidad

  def informacion(self):
    print("El saldo de la cuenta es: ", self.saldo,"$")
    print("La cuenta es de tipo: ", self.tipo)
    print("La cuenta se creó el día: ", self.fechaCreacion)

