'''
@angelismaelaivs@ciencias.unam.mx
'''
 
import csv
import os  #con esto me hice un buen de bolas para leer el archivo ToT
from Cuenta import Cuenta
 
rutaArchivo = os.path.join(os.path.dirname(__file__), 'cuentas.csv')
 
 
def guardarCuentas(cliente):
    with open(rutaArchivo, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(['mail_cliente', 'saldo', 'tipo', 'fecha_creacion'])
        for cuenta in cliente.cuentas:
            csv_writer.writerow([cliente.mail, cuenta.getSaldo(), cuenta.getTipo(), cuenta.getFechaCreacion()])
    print("Cuentas guardadas.")
 
 
def cargarCuentas(cliente):
    try:
        with open(rutaArchivo, encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)  # saltar encabezado
            for row in csv_reader:
                mail_cliente, saldo, tipo, fecha_creacion = row
                if mail_cliente == cliente.mail:
                    cuenta = Cuenta(float(saldo), tipo, fecha_creacion)
                    cliente.agregarCuenta(cuenta)
        print("Cuentas cargadas.")
    except FileNotFoundError:
        print("No hay cuentas guardadas aún.")