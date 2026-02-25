from clases import grafica
from clases import vertices
from clases import aristas

class Menu:
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
                self.grafica.agregar_vertice(v)
                print("Los vertices de la gráfica son: ", list(self.grafica.vertices.keys()))
                print("Las aristas de la gráfica son: ", [(a.vertice1, a.vertice2, a.peso) for a in self.grafica.aristas.values()])
            elif opcion == "2":
                u = input("Origen: ")
                v = input("Destino: ")
                peso = float(input("Peso: "))
                self.grafica.agregar_aristas(u, v, peso)
                print("Los vertices de la gráfica son: ", list(self.grafica.vertices.keys()))
                print("Las aristas de la gráfica son: ", [(a.vertice1, a.vertice2, a.peso) for a in self.grafica.aristas.values()])           
            elif opcion == "0":
                break 

            else:
                print("La opción no es válida. Intente con 1, 2, 3, 4 o 0.")

        

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()