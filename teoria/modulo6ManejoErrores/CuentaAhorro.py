from Cuenta import *

class CuentaAhorro(Cuenta):
    def __init__(self, saldoInicial, tInteres):
        Cuenta.__init__(self, saldoInicial)
        self.tasaInteres = tInteres
    
    def __str__(self):
        return Cuenta.__str__(self) + f'::Tasa de interes:: {str(self.tasaInteres)}'