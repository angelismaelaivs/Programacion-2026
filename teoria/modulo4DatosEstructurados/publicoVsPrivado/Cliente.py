'''
Created on march 14 !Pi Day¡ 
@angelismaelaivs@ciencias.unam.mx
'''
from Cuenta import *

#Esta clase tendrá sus atributos publicos
class Cliente:
    def __init__(self, nombre, mail, edad, cuenta):
        self.nombre = nombre 
        self.mail = mail
        self.edad = edad
        self.cuenta = cuenta  

    #Aqui ocupo el metodo getTipo()
    def __str__(self):
        return f"Nombre::{self.nombre}  ::Mail::{self.mail}  ::Edad::{self.edad} ::Cuenta:: {self.cuenta} ::Tipo:: {self.cuenta.getTipo()}"



