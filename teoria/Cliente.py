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
        return f"Nombre::{self.nombre}  ::Mail::{self.mail}  ::Edad::{self.edad}"



