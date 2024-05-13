import numpy as np

ejecicio_19 = [[0.2, 0.8, 0.3], [0.9, 0, 0], [0, 0.7, 0]]
ejecicio_20 = [[0, 0, 8], [1/4, 0, 0], [0, 1/2, 0]]

# Definir la matriz de Leslie
leslie_matrix = np.array(ejecicio_20)

# Calcular los valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(leslie_matrix)

# Obtener el vector propio asociado al valor propio 1 (valor propio dominante)
indice_valor_propio_1 = np.where(np.isclose(valores_propios, 1))
vector_propio_1 = vectores_propios[:, indice_valor_propio_1]

# Normalizar el vector propio para obtener la distribución estable de edades
distribucion_estable = vector_propio_1 / np.sum(vector_propio_1)

print("Distribución estable de edades:", distribucion_estable)
