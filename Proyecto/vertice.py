from Arista import *

class Vertice:
    def __init__(self, nombre, distanciaTotal):
        self.nombre = nombre
        # Marca la suma de las distancias entre un vértice y otro.
        self.distanciaTotal = distanciaTotal  
        # Me indica si ya visité este vértice durante el algoritmo.
        self.visitado = False
        # Aristas que salen del vértice.
        self.aristas = []

    # METODOS

    # Así creamos una arista entre 2 vértices
    def agregarArista(self):
        nuevaArista = Arista(origen, destino, distancia)
        self.aristas.append(nuevaArista)

    # Devuelve un listado de las aristas que obtuvimos al agregar aristas
    def listaAristas(self):
        return self.aristas
    
    def resetBusqueda(self):
        self.visitado = False
        # inf hace que el valor de la distanciaTotal sea mayor a cualquier distancia en mi gráfica
        self.distanciaTotal = float('inf') 


    def __str__(self):
        aristasStr = ""
        for i, arista in enumerate(self.aristas):
            aristasStr += str(arista)
            if i < len(self.aristas) -1:
                aristasStr += ", "
        return f'Nombre:: {self.nombre}, ::Distancia Total:: {self.distanciaTotal}, ::Aristas:: [{aristasStr}]'