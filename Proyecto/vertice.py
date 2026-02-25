class vertices:
    def __init__(self,nombre):
        self.nombre = nombre
        self.dist_min = float()
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
        self.aristas = {}
    
    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = vertices(nombre)
            print(f"Vértice '{nombre}' agregado.")
    def agregar_aristas(self, v_1, v_2, w):
        if v_1 not in self.vertices or v_2 not in self.vertices:
            self.agregar_vertice(v_1)
            self.agregar_vertice(v_2)
            
            return
        if w <= 0:
            print("El peso debe ser mayor a cero.")

    def vecinos(self, nombre):
        return [(u.destino, u.peso) for u in self.aristas if u.origen == nombre]