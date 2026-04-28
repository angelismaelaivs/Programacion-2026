from Cuenta import * 
from Menu import *

class Main: 
    pass


cuenta1 = Cuenta(1000.12, 'Cuenta de ahorro', '1/Enero/2010', 'Angel Ismael')

menu = Menu("BANCO CIENCIAS", cuenta1)
menu.darBienvenida()

opcion = menu.despliegaMenu()
menu.procesaOpcion(opcion)
