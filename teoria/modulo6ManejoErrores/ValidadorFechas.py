'''
Validación de fechas y manejo de errores para el sistema de banco.

@angelismaelaivs@ciencias.unam.mx
'''

from datetime import datetime

FORMATO_FECHA = '%d/%m/%Y'

def validarFecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, FORMATO_FECHA)
        if fecha.year < 1900:
            print("Error: el año no es válido.")
            return None
        return fecha
    except ValueError:
        print("Error: formato de fecha incorrecto. Use DD/MM/AAAA.")
        return None