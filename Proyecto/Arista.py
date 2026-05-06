class Arista:
    def __init__(self, origen, destino, distancia):
        #Origen y destino me marcan de que vértice a que otro vértice va mi arista.
        self.origen = origen
        self.destino = destino
        #Distancia entre 2 vertices
        self.distancia = distancia
        
    def __str__(self):
        return f'::Origen:: {self.origen.nombre}, ::Destino:: {self.destino.nombre}, ::DISTANCIA:: {self.distancia}'