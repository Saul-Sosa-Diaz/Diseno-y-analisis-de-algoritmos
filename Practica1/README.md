![](RackMultipart20230204-1-ipviye_html_9efe932347ec43c4.png)

##


## Diseño y Análisis de Algoritmos

## Práctica 2 - Simulador de la máquina RAM

**Factor de ponderación:** 8

### Descripción de una máquina RAM

Una _Máquina de Acceso Aleatorio (RAM)_ es aquella máquina teórica que se utiliza para el cálculo de la complejidad de los diferentes algoritmos en esta asignatura. Ello se debe a que posee 3 características básicas:

- No posee concurrencia.
- Sus instrucciones son de tiempo constante.
- Permite medir el número de instrucciones ejecutadas.

Una máquina RAM se estructura como se puede indica en la siguiente imagen:

![](RackMultipart20230204-1-ipviye_html_203521c0e2bf4ea9.png)

Así pues, podemos decir que la máquina RAM se divide en 5 grandes componentes:

1. **Memoria de programa:** Guarda el conjunto de instrucciones de un programa. Esta memoria **no es modificable.**
2. **Memoria de datos:** Posee una serie de registros indexados R0, R1, R2, …, Rn para almacenar datos. El registro R0 es un registro especial llamado **acumulador** , el cual ayuda en la realización de operaciones aritméticas, lógicas y de control.
3. **Unidad de aritmética, control y lógica:** Permite realizar operaciones aritméticas (ADD, SUB, DIV, etc.), de control de programa (JUMP) o lógicas (JGTZ, JZERO).
4. **Unidad de entrada:** Gestiona la entrada de datos de la máquina. La entrada de datos viene representada por una cinta de elementos, y para su lectura se dispone de un cabezal que se mueve a la siguiente posición cada vez que se realiza una operación de lectura (READ).
5. **Unidad de salida:** Gestiona la salida de datos de la máquina. La salida de datos viene representada por una cinta de elementos, y para su escritura se dispone de un cabezal que se mueve a la siguiente posición cada vez que se realiza una operación de escritura (WRITE).

La máquina posee un conjunto de instrucciones finito, cada una de ellas formada por una combinación de OPERADOR + OPERANDO, pudiendo ser el operando una etiqueta. Las instrucciones disponibles en nuestra máquina RAM serán las siguientes:

| **Instrucción** | **Descripción** |
| --- | --- |
| LOAD op | El operando se carga en R0. |
| STORE op | El contenido de R0 se guarda en la memoria según lo indicado en el operando. |
| ADD op | El operando se suma a R0 y el resultado se almacena en R0. (R0 = R0 + op) |
| SUB op | El operando se resta a R0 y el resultado se almacena en R0. (R0 = R0 - op) |
| MULT op | El operando se multiplica con R0 y el resultado se almacena en R0. (R0 = R0 \* op) |
| DIV op | El operando divide a R0 y el resultado se almacena en R0. (R0 = R0 / op) |
| READ op | Se lee un valor de la cinta de entrada y se almacena en la memoria según lo indicado en el operando. |
| WRITE op | Se escribe lo indicado por el operando en la cinta de salida. |
| JUMP etiq | El control del programa salta a la instrucción indicada por la etiqueta. |
| JZERO etiq | El control del programa salta a la instrucción indicada por la etiqueta si el valor de R0 es igual a 0 (R0 == 0). |
| JGTZ etiq | El control del programa salta a la instrucción indicada por la etiqueta si el valor de R0 es mayor a 0 (R0 \> 0). |
| HALT | Detiene la ejecución del programa. |

Además de las etiquetas, la máquina RAM define 3 tipos de operandos:

- **Operando =i** : Constante con valor i. Por ejemplo, LOAD =10 → R0 = 10. Este tipo de operando no tiene sentido para instrucciones que necesiten el valor de un registro como LOAD.
- **Operando i** : Indica el registro Ri (direccionamiento directo). Por ejemplo, LOAD 10 → R0 = R10.
- **Operando \*i** : Indica el registro contenido en el registro Ri (direccionamiento indirecto). Por ejemplo, LOAD \*10 → R0 = Ri, siendo i el contenido del registro R10.

Un programa RAM consiste en una secuencia de instrucciones que se ejecutan de manera secuencial, salvo que se encuentren sentencias de control como JUMP, JZERO o JGTZ. La ejecución del programa se hace de acuerdo a las siguientes reglas:

- La ejecución comienza en la primera instrucción del programa, con todos los registros de la memoria vacíos y con los datos de entrada cargados en la cinta de entrada.
- Se ejecuta una instrucción, se modifican los registros de memoria necesarios o la cinta de salida y, acto seguido, se pasa a la ejecución de la siguiente instrucción.
- Las instrucciones READ y WRITE leen y escriben en las cintas correspondientes, y en ambos casos se avanza una posición en la cinta. No se puede utilizar el registro R0 como operando de las instrucciones READ y WRITE. Por tanto, las instrucciones READ 0 y WRITE 0 no son válidas.
- El programa termina cuando no hay más instrucciones a ejecutar o cuando se encuentra la instrucción HALT.

La complejidad de un programa en la máquina RAM es equivalente al número de instrucciones ejecutadas por el mismo.

### Objetivos de la práctica

Los siguientes objetivos se consideran **condición necesaria pero no suficiente** para aprobar la práctica:

1. Programar un simulador de máquina RAM atendiendo a las especificaciones indicadas en la sección anterior y a los requisitos de la siguiente sección.
2. Utilizar el paradigma de **Programación Orientada a Objetos** , así como seguir los principios **SOLID** y el **patrón estrategia** en caso de ser necesario.
3. Utilizar los lenguajes de programación **C++** o **Python**.

### Requisitos evaluables del simulador RAM

Los siguientes requisitos se evaluarán de cara a la entrega de la práctica:

1. Todo el código deberá estar adecuadamente comentado y desarrollado atendiendo al paradigma de Programación Orientada a Objetos.
2. El simulador debe funcionar con los ejemplos de prueba proporcionados junto con este enunciado.
3. El programa RAM a cargar en la memoria, el contenido de la cinta de entrada y el contenido de la cinta de salida se modelarán mediante tres ficheros independientes.
4. El simulador debe ejecutarse de la siguiente manera:

**C++:**./simulador program.ram input\_tape.in output\_tape.out

**Python:** python simulador.py program.ram input\_tape.in output\_tape.out

Donde cada parámetro de entrada al programa significa lo siguiente:

- ram: Fichero con el programa RAM.
- input\_tape.in: Fichero con el contenido de la cinta de entrada.
- utput\_tape.out: Fichero con el contenido de la cinta de salida.

1. Las instrucciones de la máquina RAM pueden estar escritas en mayúscula o en minúscula.
2. Se pueden especificar comentarios en un programa RAM, indicados por el carácter #. La línea que empiece por # no se cargará como parte del programa RAM.
3. Se deben contemplar los 3 tipos de operandos: constante, direccionamiento directo y direccionamiento indirecto.
4. Se debe comprobar que las instrucciones sean válidas. Sólo se permiten las instrucciones ya especificadas en la tabla correspondiente, con el formato indicado en la misma. Por ejemplo, la instrucción STORE =3 no es válida, ya que STORE no permite un comando de tipo constante.
5. Si se detecta algún error se debe imprimir en la consola un mensaje que indique la instrucción errónea y el número de línea dentro del programa RAM que lo provocó.
6. Cuando se alcance una instrucción HALT o se detecte un error, el contenido de la cinta de salida debe volcarse en el fichero indicado.

Durante la defensa de la práctica **se podrá solicitar algún tipo de modificación o prueba adicional** , la cual afectará en diferente grado a la nota final.

### Entrega de la práctica

La práctica debe entregarse en tiempo y forma acorde a lo indicado en la tarea del campus virtual. Para poder considerar la práctica como aprobada, deben cumplirse 2 requisitos:

- La práctica debe defenderse en su sesión correspondiente. Además, debe funcionar tal y como se especifica en el presente enunciado.
- Se debe entregar la tarea del campus virtual incluyendo un fichero con extensión **tar.gz** con el código fuente del programa.

La no realización de uno de estos 2 puntos conlleva la calificación como suspenso de la práctica.