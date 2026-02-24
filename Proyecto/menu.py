import clases

def __init__(self):
    self.grafica = grafica()

def mostrar_menu(self): #por ahora solo funcionara 1, 2 y 0
        print("\n--- MENÚ DIJKSTRA ---")
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