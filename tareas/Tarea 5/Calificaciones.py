# Creado el 07-05-2026
# @angelismaelaivs

calificaciones = {'A+':10, 'A':9, 'B':8, 'C':7, 'D': 6, 'F':5 }

while True:
    calificacion = input('Mi calificación es:').upper().strip()

    if calificacion == '':
        print('Saliendo del programa :) ...')
        break

    try:
        print(f'Tu calificacion en escala numérica es: {calificaciones[calificacion]}')
        
    except KeyError:
        try:
            numero = int(calificacion)
            encontrado = False
            for clave, valor in calificaciones.items():
                if valor == numero:
                    print(f'Tu calificacion en escala de letras es: {clave}')
                    encontrado = True
                    break
            if not encontrado:
                print(f'{numero} no corresponde a ninguna calificación, ingresa alguna de las siguientes (5,6,7,8,9,10)')
        
        except ValueError:
            print(f'{calificacion} no es una calificacion valida, ingresa una letra de la lista (A+,A,B,C,D,F).' )