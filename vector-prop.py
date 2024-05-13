import numpy as np

ejecicio_15 = [[1, 2], [-1, 4]]
ejecicio_16 = [[4, 0, 0], [1, 3, 0], [2, 1, -1]]
ejecicio_17 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
ejecicio_18 = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]

# Definir la matriz A y el valor propio λ
A = np.array(ejecicio_17)

valor_propio = 3

# Restar λ * I de la matriz A
A_lambda = A - valor_propio * np.eye(A.shape[0])

# Encontrar el espacio nulo de la matriz resultante
_, vectores_propios = np.linalg.eig(A_lambda)

vector_propio = vectores_propios[:, 0]

print("Vector propio correspondiente a λ =", valor_propio, ":", vector_propio)
