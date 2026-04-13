#Tarea 2
Actualmente, nuestras clases de operación (Suma, Resta, Producto, Potencia) no saben calcular un resultado, ni mostrarlo en fomrato latex.

-Implementa el método evaluar en cada clase.
-Implementa el metodo latex() en todas las clases, y en particular para para Variable considera para que si el nombre tiene más de una letra (como "alpha"), le agregue una barra invertida \ al principio.
-Asegúrate de que todas las clases de operación puedan recibir un número de Python por la izquierda (usando métodos r...) para que el orden de los factores no altere el producto... ¡ni rompa el código!"


Por ultimo prueba con este ejemplo:


x = Variable("x")
y = Variable("alpha")

expr = (x + 2) * (y - 5)**2
     
Visualiza la expresión, y evalua: x = 10, y alpha = 8