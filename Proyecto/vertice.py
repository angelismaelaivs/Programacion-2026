from Arista import *

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distanciaTotal = float('inf') 
        self.visitado = False
        self.aristas = []
        self.predecesor = None


    def agregarArista(self, origen, destino, distancia):
        nuevaArista = Arista(origen, destino, distancia)
        self.aristas.append(nuevaArista)

    def listaAristas(self):
        return self.aristas
    
    def resetBusqueda(self):
        self.visitado = False
        self.distanciaTotal = float('inf')
        self.predecesor = None

    def __str__(self):
        aristasStr = ""
        for i, arista in enumerate(self.aristas):
            aristasStr += str(arista)
            if i < len(self.aristas) -1:
                aristasStr += ", "
        return f'Nombre:: {self.nombre}, ::Distancia Total:: {self.distanciaTotal}, ::Aristas:: [{aristasStr}]'