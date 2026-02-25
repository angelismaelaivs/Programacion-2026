from vertice import Vertice

def main():
    print("=== Crear un Vértice ===")
    
    nombre = input("Ingresa el nombre del vértice (una letra): ")
    peso = float(input("Ingresa el peso del vértice (número positivo): "))
    
    v = Vertice(nombre, peso)
    
    print("\nVértice creado:")
    print("Nombre:", v.nombre)
    print("Peso:", v.peso)

if __name__ == "__main__":
    main()