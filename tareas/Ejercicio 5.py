#  i. Construye un programa que diga si un número entero es o no primo
# ii. Elabora un programa que muestre los primeros N números primos. (N es solicitao por el usuario).

class Numeros:
    def __init__(self):
        pass

    def mostrarOpciones(self):
        print('1. Determinar si un numero es primo.')
        print('2. Mostrar los primeros N números primos')

    def determinarPrimo(self, numero):
        i=2
        while i <= numero**0.5:
            resultado = numero/i
            if resultado == int(resultado):
                return False
            i += 1
        else:
            return True
    def mostrarPrimos(self, N):
        contador = 0
        numero = 2

        while contador < N:
            if self.determinarPrimo(numero) == True:
                print(numero)
                contador += 1
            numero += 1


    def procesarOpcion(self,opcion):
        while True:
            if opcion == 1:
                print('Escogió determinar si un número es primo, ingrese el número deseado:')
                n = int(input())
                self.determinarPrimo(n)
                if self.determinarPrimo(n):
                    print('El número es primo.')
                elif self.determinarPrimo(n) == False:
                    print('El número no es primo')
            elif opcion == 2:
                print('Escogio mostrar los primeros N números primos, ¿hasta que numero quieres?')
                n = int(input())
                print('Los primeros ', n, 'números primos son:')
                self.mostrarPrimos(n) 
                break

num = Numeros()
print('Elije  alguna de las opciones:')
num.mostrarOpciones()

try:
    opcion = int(input())
    num.procesarOpcion(opcion)
except ValueError:
    print('Debes de elegir un numero de la lista de opciones.')



