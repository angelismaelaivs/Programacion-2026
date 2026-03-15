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

    def __str__(self):
        return "Nombre::" + srt(self.nombre) + " ::Mail::" + str(self.mail) + " ::Edad::" + self.edad

cliente1 = ("Angel", "angelismaelaivs@ciencias.unam.mx", 22)

print(str(cliente1))