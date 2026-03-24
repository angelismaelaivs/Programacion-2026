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

    def __str__(self):
        return f"Nombre::{self.nombre}  ::Mail::{self.mail}  ::Edad::{self.edad} ::Cuenta:: {self.cuenta}"



