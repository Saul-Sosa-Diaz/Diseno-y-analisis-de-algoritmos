import numpy as np
import os

def generateProblems():
    '''
    It generateProblemss a random matrix of size (rows, columns) with elements rounded to 2 decimals.
    '''
    for i in range(0,1):
        rows = np.random.randint(low=10, high=30) # Numero mínimo de puntos 10, maximo 200
        columns = np.random.randint(low=2, high=5) # Dimension de los puntos minima 2 maxima 10
        coordenateOfPoints = np.round(np.random.uniform(
            low=0.0, high=15.0, size=(rows, columns)), decimals=2)
  
        
        lists = np.array(coordenateOfPoints)

        # Recorrer todas las filas del list y convertirlas a strings de texto
        strings = []
        for row in lists:
            # Convertir cada elemento de la fila a una string de texto
            string = [str(element) for element in row]
            # Reemplazar los puntos por comas en cada elemento de la string
            string = [element.replace('.', ',') for element in string]
            # Unir los elementos de la string en una sola string separada por espacios
            new_string = ' '.join(string)
            # Agregar la nueva string a la lista de strings
            strings.append(new_string)

        # Imprimir todas las strings separadas por saltos de línea
        strings = '\n'.join(strings)
        rows
        columns

        # Nombre del directorio a crear
        directory = 'problems'

        # Crear el directorio si no existe
        if not os.path.exists(directory):
            os.makedirs(directory)

        nameFile = "prob" + str(i+3) + ".txt"
        # Ruta del archivo dentro del directorio
        pathFile = os.path.join(directory, nameFile)
        toFile = str(rows) + "\n" + str(columns) + "\n" + strings
        with open(pathFile, 'w') as archivo:
            archivo.write(toFile)

generateProblems()