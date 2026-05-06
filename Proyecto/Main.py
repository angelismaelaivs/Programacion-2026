from Grafica import *
from Vertice import *
from Arista import *

class Main:
    pass


#Prueba de leerMatriz
nombres = ["A", "B", "C", "D"]

matriz = [
        [0, 4, 2, 0],
        [0, 0, 0, 5],
        [0, 1, 0, 8],
        [0, 0, 0, 0]
        ]

g = Grafica()
g.leerMatriz(nombres, matriz)

print(g)

verticePrueba = g.obtenerVertice("A")
print(verticePrueba.nombre)
print(verticePrueba.distanciaTotal)

for arista in verticePrueba.aristas:
    print(arista)