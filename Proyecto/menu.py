from clases import grafica
from clases import vertices
from clases import aristas


def __init__(self):
    self.grafica = grafica()

def mostrar_menu(self): #por ahora solo funcionará 1, 2 y 0 ya que aun no hago el algoritmo de Dijkstra y el camino mínimo
        while True:
            print("\n--- Seleccione una opción ---")
            print("1. Agregar vértice")
            print("2. Agregar arista")
            print("3. Ejecutar Dijkstra") 
            print("4. Mostrar camino mínimo") 
            print("0. Salir")
        
            opcion = input("Opción: ")

            if opcion == "1":
                v = input("Vértice: ")
                grafica.agregar_vertice(v)

            elif opcion == "2":
                u = input("Origen: ")
                v = input("Destino: ")
                peso = float(input("Peso: "))
                grafica.agregar_arista(u, v, peso)
            
            elif opcion == "0":
                break 

            else:
                print("La opción no es válida. Intente con 1, 2, 3, 4 o 0.")