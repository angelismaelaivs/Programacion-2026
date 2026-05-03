'''
Created on march 14 !Pi Day¡ 
@angelismaelaivs@ciencias.unam.mx
'''
from Cuenta import *

class Cliente:
    def __init__(self, nombre, mail, edad):
        self.nombre = nombre 
        self.mail = mail
        self.edad = edad
        self.cuentas = [] 

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminarCuenta(self, nombreDeCuenta):
        self.cuentas.remove(nombreDeCuenta) 

    def informacionCuentas(self):
        print("---Cantidad de Cuentas: " + str(len(self.cuentas)) + " ---")
        if len(self.cuentas) == 0:
            print("No hay cuentas registradas.")
        else:
            for i, cuenta in enumerate(self.cuentas, 1):
                print(i, '. ', cuenta)


    def __str__(self):
        tmp = "Nombre::" + str(self.nombre)
        tmp += "\nMail::" + str(self.mail)
        tmp += "\nEdad::" + str(self.edad)
        return tmp