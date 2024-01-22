#app_1.51
import numpy as np
import time
# Creamos dos vectores aleatorios
tamano = 10000
np.random.seed(0)
vector_1 = np.random.random(tamano)
vector_2 = np.random.random(tamano)
# Implementación del producto vectorial en Python
instante_inicial = time.process_time()
producto_con_python = np.zeros((tamano, tamano))
for i in range(tamano):
    for j in range(tamano):
        producto_con_python[i][j] = vector_1[i] * vector_2[j]
        phyton_tiempo = time.process_time() - instante_inicial
# Implementación del producto vectorial Numpy
instante_inicial = time.process_time()
producto_con_numpy = np.outer(vector_1, vector_2)
numpy_tiempo = time.process_time() - instante_inicial
# Evaluación de resultados
if (producto_con_numpy == producto_con_python).all():
    print('Los resultados son iguales')
else:
    print('Los resultados son diferentes')
print('Tiempo de Python', phyton_tiempo)
print('Tiempo de Numpy', numpy_tiempo)
print('Mejora con Numpy', phyton_tiempo / numpy_tiempo)