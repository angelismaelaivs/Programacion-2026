class vertices:
    def __init__(self,nombre):
        self.nombre = nombre
        self.dist_min
        self.visitado = False
        self.previo = None

class aristas:
    def __init__(self, v_1, v_2, w):
        self.vertice1 = v_1
        self.vertice2 = v_2
        self.peso = w

class grafica:
    def __init__(self,):
        self.vertices = {}
        self.aristas = []
    
    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = self.vertices(nombre)

    def agregar_aristas(self, v_1, v_2, w):
        if v_1 not in self.vertices or v_2 not in self.vertices:
            print("No existen tales vértices, introduce vertices que sí existan en la gráfica.")
            return

    def vecinos(self, nombre):
        return [(u.destino, u.peso) for u in self.aristas if u.origen == nombre]