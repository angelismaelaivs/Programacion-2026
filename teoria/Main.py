from Cuenta import * 
from Menu import *

class Main: 
    pass

cuenta1 = Cuenta(2.10, 'Cuenta de ahorro', '27/Diciembre/2010')

menu = Menu("BANCO CIENCIAS", cuenta1)
menu.darBienvenida()
menu.despliegaMenu()
    




