# Práctica 7 - Práctica K-means: 
* author: Saúl Sosa Díaz
* email: _alu0101404141@ull.edu.es_
* Overleaf: https://es.overleaf.com/read/fgfqckphwchq

## Resumen
K- Means es un algoritmo de agrupamiento muy simple. En primer lugar, selecciona un
conjunto de k centroides. A continuación, asigna cada punto al centroide más cercano.
Finalmente, recalcula el centroide de cada cluster y repite estos dos últimos pasos hasta
que ningún punto cambie de cluster. En la figura 1 se muestra un pseudocódigo del
algoritmo K-Means.

1. Seleccionar K puntos como centroides iniciales
2. repeat
3.   Construir K clusters asignando cada punto al centroide más cercano;
4.   Recalcular los centroides de cada cluster;
5. until (Ningún punto cambie de cluster)



## Ejecución
**El programa generará una instancia aleatoria por defecto. Si se quisiera cambiar habría que indicarle el parámetro -f**  
El fichero `main` está en la carpeta /src, para ejecutar el programa ejecute el siguiente programa:

```BASH
python3 ./src/main.py
```

## Opciones del programa
 * -f < Ruta al fichero con las coordenadas de los puntos > -> Sirve para indicar el fichero con las coordenadas de los puntos.
 * -o < Nombre del fichero de salida donde se volcarán los datos > -> Sirve para indicar el fichero con las coordenadas donde se guardarán los datos.
 * -k < Numero de clusters > -> Inidica el número de clusters que los algoritmos tendrán en cuenta. 3 Por defecto
 * -c < Cardinalidad de la lista de candidatos > -> Inidica la cardinalidad de la lista de candidatos.
 3 por defecto.


## Ayuda
Para ver las opciones del programa:
```BASH
python3 ./src/main.py -h
```


**IMPORTANTE**: Para ejecutar este programa son necesarias las siguientes librerías:,
* [Numpy](https://numpy.org/doc/stable/index.html): Es el paquete fundamental para la computación científica en Python. Se trata de una biblioteca de Python que proporciona un objeto array multidimensional.
* [Typeguard](https://pypi.org/project/typeguard/): Se utiliza para comprobar en tiempo de ejecución que los argumentos pasados a una función coinciden con los tipos de datos esperados.


## Estructura de directorios
```
  .
  ├── src            # Implementación del problema
  └── problems       # Directorio con problemas
```

## Referencias:
* [Numpy](https://numpy.org/doc/stable/index.html)
* [Github repository](https://github.com/Saul-Sosa-Diaz/Diseno-y-analisis-de-algoritmos.git)
* [Typeguard](https://pypi.org/project/typeguard/)


[Python website]: <https://www.python.org/downloads/>
