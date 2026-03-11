from Cuenta import * 
from Menu import *

class Main: 
    pass

    cuenta1 = Cuenta(1000.12, 'Cuenta de ahorro', '1/Enero/2010')
    menu = Menu("BANCO CIENCIAS", cuenta1)
    menu.darBienvenida()
    
    continuar = True
    while continuar:
        menu.despliegaMenu()
        opcion = input('Elige una opción:')
        continuar = menu.procesaOpcion(opcion)
        
    




