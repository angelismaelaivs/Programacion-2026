from Cuenta import *

class CuentaHija(Cuenta):                        
 
    def __init__(self, valor, tipo):
        Cuenta.__init__(self, valor)             
        self.__tipo = tipo
 
 
    def __str__(self):
        
        return Cuenta.__str__(self) + f"  ::Tipo :: {self.__tipo}"