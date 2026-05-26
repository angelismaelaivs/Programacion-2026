from Cuenta import *

class CuentaHija(Cuenta):                        
 
    def __init__(self, valor, tipo):
        Cuenta.__init__(self, valor)             # estilo clásico (igual que super())
        self.__tipo = tipo
 
    # b) depositar() NO se redefine → se hereda directamente de Cuenta ✓
 
    def __str__(self):
        '''
        c) Redefinimos __str__ porque la madre no conoce el tipo.
        '''
        return Cuenta.__str__(self) + f"  ::Tipo :: {self.__tipo}"