from Cuenta import * 
from Menu import *
from Cliente import *

class Main: 
    pass
    menu = Menu("BANCO CIENCIAS")
    menu.darBienvenida()

    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion)


cuenta1 = Cuenta(1000.12, 'Cuenta de ahorro', '1/Enero/2010')
cliente1 = Cliente("Angel", "angelismaelaivs@ciencias.unam.mx", 22, cuenta1)  #Aqui relaciono Cliente con Cuenta

