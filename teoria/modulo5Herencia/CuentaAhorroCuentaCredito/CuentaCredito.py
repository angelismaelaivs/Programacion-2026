from Cuenta import *
 
class CuentaCredito(Cuenta):
    
    def __init__(self, saldoInicial, mSobregiro):
        Cuenta.__init__(self, saldoInicial)
        self.montoSobregiro = mSobregiro
 
    
    def __str__(self):
        msg = Cuenta.__str__(self)
        msg += ":Monto de Sobregiro:" + str(self.montoSobregiro)
        return msg
 
    def retirar(self, valor):
        result = True
 
        if self.cantidad < valor:
            # No hay saldo suficiente, revisar si el sobregiro cubre
            sobregiroNecesario = valor - self.cantidad
            if self.montoSobregiro < sobregiroNecesario:
                # Tampoco alcanza el sobregiro
                print("No se pudo retirar")
                result = False
            else:
                # El sobregiro cubre la diferencia
                self.cantidad = 0.0
                self.montoSobregiro -= sobregiroNecesario
        else:
            # Saldo suficiente, retiro normal
            self.cantidad = self.cantidad - valor
 
        return result