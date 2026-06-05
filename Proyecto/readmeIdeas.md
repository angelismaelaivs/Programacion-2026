# IDEAS Y PROGRESO

- Clase: vertices, aristas y grafica
- Clase: Visitar nodos; esta clase verificara la distancia entre nodos y entonces segun la distancia los visitará o no.




# ALGORITMO PRINCIPAL

DIJKSTRA(grafica, origen, destino):

1. Establecer nodoOrigen._distanciaTotal = 0

2. Crear lista "pendientes" con todos los nodos de la gráfica

3. MIENTRAS pendientes no esté vacía:

    a. De "pendientes", tomar el nodo con menor _distanciaTotal
       → llamarlo "actual"

    b. Si actual == destino → TERMINAR (ya encontramos el camino)

    c. Marcar actual._visitado = True
       Quitar actual de "pendientes"

    d. PARA CADA arista en actual.obtener_aristas():
          vecino = arista.destino
          SI vecino no ha sido visitado:
              nueva_distancia = actual._distanciaTotal + arista.distancia
              SI nueva_distancia < vecino._distanciaTotal:
                  vecino._distanciaTotal = nueva_distancia

4. Reconstruir el camino desde destino hasta origen
   siguiendo los nodos de menor _distanciaTotal

5. Regresar camino y distanciaTotal del nodo destino