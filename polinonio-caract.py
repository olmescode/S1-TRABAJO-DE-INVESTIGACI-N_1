import numpy as np

ejecicio_1 = [[1, 2], [2, -1]]
ejecicio_2 = [[1, 1], [-2, 4]]
ejecicio_3 = [[2, 1], [-1, 3]]
ejecicio_4 = [[2, 4, 0], [1, 2, 1], [0, 4, 2]]
ejecicio_5 = [[1, 2, 1], [0, 1, 2], [-1, 3, 2]]
ejecicio_6 = [[4, -1, 3], [0, 2, 1], [0, 0, 3]]
ejecicio_7 = [[2, 1, 2], [2, 2, -2], [3, 1, 1]]
ejecicio_8 = [[1, 0, 0, 0], [2, -2, 0, 0], [0, 0, 2, -1], [0, 0, -1, 2]]

# Definir la matriz
matriz = np.array(ejecicio_8)

# Calcular el polinomio característico
polinomio_caracteristico = np.poly(matriz)

# Redondear los coeficientes del polinomio característico
polinomio_caracteristico_redondeado = np.round(polinomio_caracteristico, decimals=2)

print("Polinomio característico:", polinomio_caracteristico_redondeado)

