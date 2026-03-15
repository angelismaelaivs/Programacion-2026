from Cuenta import * 
from Menu import *
from Cliente import *

class Main: 
    pass

    menu = Menu("BANCO CIENCIAS")
    menu.darBienvenida()

    continuar = True
    while continuar:
        menu.despliegaMenu()
        opcion = input('Elige una opción:')
        continuar = menu.procesaOpcion(opcion)
        


