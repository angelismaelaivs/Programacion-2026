'''
Created on march 14 !Pi Day¡ 
@angelismaelaivs@ciencias.unam.mx
'''
from Cuenta import *

class Cliente:
    def __init__(self, nombre, mail, edad, cuenta):
        self.nombre = nombre 
        self.mail = mail
        self.edad = edad
        self.cuenta = cuenta   #Aqui hago una relación entre la clase Cuenta y Cliente

    def informacion( self ):
        print('Nombre::', self.nombre)
        print('Mail::', self.mail)
        print('Edad::', self.edad)
        self.cuenta.informacion()  #Aqui se usan los metodos de la clase Cuenta