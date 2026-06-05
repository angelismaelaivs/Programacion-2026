from Cuenta import * 
from Menu import *
from Cliente import *
from GestorCuentas import *

class Main: 
    pass

cliente1 = Cliente("Angel", "angelismaelaivs@ciencias.unam.mx", 22)

cargarCuentas(cliente1)

menu = Menu("BANCO CIENCIAS", cliente1)
menu.darBienvenida()
menu.desplegarMenu()
