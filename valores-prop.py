import numpy as np

ejecicio_9 = [[1, -3], [3, -5]]
ejecicio_10 = [[2, 4], [3, 6]]
ejecicio_11 = [[3, -1, 4], [-1, 0, 1], [4, 1, 2]]
ejecicio_12 = [[2, -2, 0], [1, -1, 0], [1, -1, 0]]
ejecicio_13 = [[0, 1, 2], [0, 0, 3], [0, 0, 0]]
ejecicio_14 = [[1, 0, 0], [-1, 3, 0], [3, 2, -2]]

# Definir la matriz
matriz = np.array(ejecicio_14)

# Calcular los valores propios
valores_propios = np.linalg.eigvals(matriz)
print("Valores propios:", valores_propios)
