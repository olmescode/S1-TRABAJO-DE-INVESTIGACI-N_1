import numpy as np

# Definir la matriz
matriz = np.array([[2, 4, 0], [1, 2, 1], [0, 4, 2]])

"""
# Calcular el polinomio característico
polinomio_caracteristico = np.poly(matriz)
print("Polinomio característico:", polinomio_caracteristico)
"""

"""
# Calcular los valores propios
valores_propios = np.linalg.eigvals(matriz)
print("Valores propios:", valores_propios)
"""

"""
# Determinar un vector propio correspondiente a un valor propio específico:

# Valor propio específico
valor_propio = -1

# Calcular los vectores propios y los valores propios
valores_propios, vectores_propios = np.linalg.eig(matriz)

# Encontrar el índice del valor propio específico
indice_valor_propio = np.where(np.isclose(valores_propios, valor_propio))

# Obtener el vector propio correspondiente
vector_propio = vectores_propios[:, indice_valor_propio]

print("Vector propio correspondiente a lambda =", valor_propio, ":", vector_propio)
"""
