from Cuenta import * 
from Menu import *
from Cliente import *

class Main: 
    pass

cliente1 = Cliente("Angel", "angelismaelaivs@ciencias.unam.mx", 22)

cuenta1 = Cuenta(1000.12, 'Cuenta de ahorro', '1/Enero/2010')
cliente1.agregarCuenta(cuenta1)

# Crear menú y ejecutar
menu = Menu("BANCO CIENCIAS", cliente1)
menu.darBienvenida()
menu.desplegarMenu()
