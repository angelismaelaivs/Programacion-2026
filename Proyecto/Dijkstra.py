from Grafica import *

class Dijkstra:

    def __init__(self, grafica):
        self._grafica = grafica

    def buscar(self, nombreOrigen, nombreDestino):

        # Vertices de origen y destino
        origen  = self._grafica.obtenerVertice(nombreOrigen)
        destino = self._grafica.obtenerVertice(nombreDestino)

        # Paso 1 README
        origen.distanciaTotal = 0

        # Lista de vértices pendientes por visitar
        pendientes = list(self._grafica.vertices)

        # Paso 2, 3 y 4 — Repetir mientras haya pendientes
        while len(pendientes) > 0:

            # Paso 2 — Elegir el vértice no visitado con menor distanciaTotal
            actual = self._elegirMinimo(pendientes)

            if actual == destino:
                camino = self._reconstruirCamino(destino)
                print(f'\nDistancia mínima de {nombreOrigen} a {nombreDestino}: {destino.distanciaTotal}')
                print(f'El camino es: {'-->'.join(camino)}')

                break

            # Paso 3 — Relajación: revisar cada arista del vértice actual
            for arista in actual.aristas:
                vecino = arista.destino

                if not vecino.visitado:
                    nuevaDistancia = actual.distanciaTotal + arista.distancia

                    # Si encontramos un camino más corto, lo actualizamos
                    if nuevaDistancia < vecino.distanciaTotal:
                        vecino.distanciaTotal = nuevaDistancia
                        # Guardamos el predecesor para reconstruir el camino de costo mínimo
                        vecino.predecesor = actual

            # Paso 4 — Marcar como visitado y quitar de pendientes
            actual.visitado = True
            pendientes.remove(actual)
        

    def _elegirMinimo(self, pendientes):
        minimo = pendientes[0]
        for vertice in pendientes:
            if vertice.distanciaTotal < minimo.distanciaTotal:
                minimo = vertice
                
        return minimo
    
    def _reconstruirCamino(self, destino):
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual.nombre)
            actual = actual.predecesor
        camino.reverse() # Invierte el orden de la lista :)
        
        return camino