from Cuenta import *
class CuentaHija(Cuenta):                        
 
    def __init__(self, valor, tipo):
        Cuenta.__init__(self, valor)             # estilo clásico (igual que super())
        self.__tipo = tipo
 
    # b) depositar() NO se redefine → se hereda directamente de Cuenta ✓
 