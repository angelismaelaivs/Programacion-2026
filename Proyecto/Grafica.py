from Vertice import *
from Arista import *

class Grafica:
    def __init__(self):
        self.vertices = []

    def leerMatriz(self, nombres, matriz):

        # Le damos nombres a los vértices de la matriz 
        for nombre in nombres:
            self.vertices.append(Vertice(nombre))

        # Range genera numeros del 0 al n-1 con n el número de filas de la matriz
        # Consideramos la columna i en nuestro listado   
        for i in range(len(matriz)):
            #Tomamos el elemento en la fila i columna j (matriz[i] devuelve el numero de columnas en la fila i)
            for j in range(len(matriz[i])):
                if matriz[i][j] != 0: #nos fijamos si hay una arista entre i y j
                    origen = self.vertices[i]
                    destino = self.vertices[j]
                    distancia = matriz[i][j]
                    origen.agregarArista(origen, destino, distancia)
    
    def obtenerVertice(self, nombre):
        for vertice in self.vertices:
            if vertice.nombre == nombre:
                return vertice
    
    def __str__(self):
        resultado = "=== Grafica ===\n"
        for vertice in self.vertices:
            resultado += str(vertice) + "\n"
        return resultado