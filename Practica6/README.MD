# Práctica 6 - Problema del Viajante de Comercio (TSP): 
* author: Saúl Sosa Díaz
* email: _alu0101404141@ull.edu.es_

## Resumen
Para la presente práctica se pide la creación de un software que, mediante el uso de herencia, resuelva el TSP de 3 formas diferentes;
 * Mediante un algoritmo de fuerza bruta. Esto implica probar todas las posibles combinaciones y devolver aquella que retorna mejores resultados.
 * Mediante un algoritmo voraz (no exacto). En este algoritmo, se parte de un nodo y en cada momento se elige la ciudad más cercana a la que se pueda desplazar (es decir, por la que no haya pasado ya).
 * Mediante un algoritmo de programación dinámica. Deben diseñar este algoritmo de cara a la práctica.  

El problema del viajante de comercio o Travelling Salesman Problem (TSP) es un problema NP-Duro altamente conocido en la literatura científica. Existe un comercial que parte de uno de los nodos y para el que se debe obtener la ruta que cumpla lo siguiente:
 * Debe pasar por todos los nodos del grafo exactamente una vez.
 * Debe volver al nodo de origen.
 * La distancia total de la ruta debe ser mínima.


## Ejecución
El fichero `main` está en la carpeta /src, para ejecutar el programa ejecute el siguiente programa:
```BASH
python3 ./src/main.py
```

## Opciones del programa
 * -d < Ruta al directorio con los ficheros de prueba > -> Sirve para indicar el directorio donde se encuentran los ficheros de los problemas
 * -t < float > -> Cambia el tiempo límite de la ejecución de los algoritmos, en segundos

## Ayuda
Para ver las opciones del programa:
```BASH
python3 ./src/main.py -h
```



**IMPORTANTE**: Para ejecutar este programa son necesarias las siguientes librerías:,
* [Tabulate](https://pypi.org/project/tabulate/): Permite crear tablas a partir de datos en una variedad de formatos, como listas, diccionarios y tuplas. Es útil para representar y visualizar datos de una manera clara y organizada.
* [Numpy](https://numpy.org/doc/stable/index.html): Es el paquete fundamental para la computación científica en Python. Se trata de una biblioteca de Python que proporciona un objeto array multidimensional.


## Estructura de directorios
```
  .
  ├── src            # Implementación del problema
  └── problems       # Directorio con problemas
```

## Referencias:
* [Tabulate](https://pypi.org/project/tabulate/)
* [Numpy](https://numpy.org/doc/stable/index.html)
* [Github repository](https://github.com/Saul-Sosa-Diaz/Diseno-y-analisis-de-algoritmos.git)


[Python website]: <https://www.python.org/downloads/>
