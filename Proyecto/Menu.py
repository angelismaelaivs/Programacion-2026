from Grafica import *
from Dijkstra import *

class Menu:

    def __init__(self):
        self._grafica = Grafica()
        self._dijkstra = None

    def iniciarMenu(self):
        print("╔══════════════════════════════════════╗")
        print("║   Bienvenido al resolutor de Dijkstra  ║")
        print("╚══════════════════════════════════════╝\n")

        self._pedirGrafica()
        self._pedirBusqueda()

    # ── Métodos privados ──────────────────────

    def _pedirGrafica(self):
        print("=== Ingresar Gráfica ===")

        # Pedir nombres de los vértices
        entrada = input("Ingresa los nombres de los vértices separados por coma (ej: A,B,C,D): ")
        nombres = entrada.split(",")
        nombres = [n.strip() for n in nombres]  # Quitamos espacios extra

        # Pedir el número de vértices para saber el tamaño de la matriz
        n = len(nombres)
        print(f"\nIngresa la matriz de adyacencia {n}x{n} fila por fila.")
        print("Usa 0 si no hay conexión entre dos vértices y enteros positivos para el peso de las aristas entre vértices.")
        print(f"Los vértices en orden son: {nombres}\n")

        matriz = []
        for i in range(n):
            while True:
                try:
                    fila = input(f"Fila {nombres[i]}: ")
                    valores = fila.split(",")
                    if len(valores) != n:
                        print(f"Error: debes ingresar exactamente {n} valores.")
                        continue
                    fila_int = [int(v.strip()) for v in valores]
                    if any(v < 0 for v in fila_int):
                        print("Error: los valores no pueden ser negativos.")
                        continue
                    matriz.append(fila_int)
                    break
                except ValueError:
                    print("Error: ingresa solo números enteros separados por coma.")

        self._grafica.leerMatriz(nombres, matriz)
        self._dijkstra = Dijkstra(self._grafica)
        print("\nGráfica cargada correctamente.")
        print(self._grafica)

    def _pedirBusqueda(self):
        print("=== Buscar Camino Mínimo ===")

        while True:
            while True:
                origen = input("Ingresa el vértice origen: ").strip()
                if self._grafica.obtenerVertice(origen) is None:
                    print(f"Error: el vértice '{origen}' no existe en la gráfica.")
                else:
                    break

            while True:
                destino = input("Ingresa el vértice destino: ").strip()
                if self._grafica.obtenerVertice(destino) is None:
                    print(f"Error: el vértice '{destino}' no existe en la gráfica.")
                else:
                    break

            self._grafica.resetBusqueda()
            self._dijkstra.buscar(origen, destino)

            otraBusqueda = input('¿Quieres buscar otro camino? (s/n):'.strip().lower())
            if otraBusqueda != 's':
                print('¡Hasta luego¡ :)')
                break