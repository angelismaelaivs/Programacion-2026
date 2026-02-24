# PROYECTO
En esta carpeta esta destinada para los archivos para mi proyecto del curso de Programacion-2026

Mi proyecto consta en un software resolutor de caminos mínimos en gráficas simples y pesos positivos con el algoritmo de Dijkstra

---
## Definiciones:

- **Gráfica simple ponderada:** Una gráfica simple es un par ordenado (V,E) de un conjunto de vertices  no vacío (V) y un conjunto de aristas (E) que cumplen las siguientes caracteristicas:
    + Sin lazos: No hay arista que conecte un vértice consigo mismo.
    + Sin aristas múltiples: Solo puede existir una arista (o ninguna) conectando cualquier par de vértices.
    + Aristas no dirigidas: El orden de los vértices en una arista no importa {u,v}={v,u}
- **Gráfica ponderada:** Dada una gráfica G=(V,E) se considera un tercer conjuto W que consta de una funcion W:V-->R donde se le asigna un "peso" a cada uno de los vertices de G.

- **Algoritmo de Dijkstra:** Dijkstra calcula los caminos mínimos desde un vértice fuente en gráficas ponderadas con
pesos positivos.
    1. Inicialización:
        Asigna a todos los nodos una distancia infinita.
        Al nodo origen asígnale distancia 0.
        Marca todos los nodos como no visitados.
    2. Selección del nodo actual    
        Elige el nodo no visitado con la menor distancia provisional.
        Este nodo será el nodo actual.
    3. Relajación de aristas
        Para cada vecino no visitado del nodo actual:
        Calcula la distancia desde el origen pasando por el nodo actual.
        Si esta distancia es menor que la distancia conocida, actualízala.
    4. Marcar como visitado
        Marca el nodo actual como visitado.
        Una vez visitado, su distancia ya no se vuelve a modificar.
    5. Repetición
        Repite los pasos 2 a 4 hasta que:
        Todos los nodos estén visitados, o
        Se haya alcanzado el nodo destino.
    6. Resultado
        Las distancias finales representan los caminos más cortos desde el origen a cada nodo.