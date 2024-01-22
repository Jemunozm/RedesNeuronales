import time
import os
import tensorflow as tf
import numpy as np


# TAMAÑO DE LA MATRIZ: SIZExSIZE
SIZE = 10000
a = np.random.rand(SIZE, SIZE)
b = np.random.rand(SIZE, SIZE)
result = np.zeros((SIZE, SIZE))

print('Producto de dos Matrices de orden 500x500')


# CONSULTAR SI TF ESTA USANDO gpu
#gpus = tf.config.experimental.list_physical_devices('GPU')
#if gpus:
#    print('GPU is available')

# CÁLCULO CON CPU Y PHYTHON
#inicio = time.time()
#for i in range(SIZE):
#    for j in range(SIZE):
#        for k in range(SIZE):
#            result[i,j] += a[i,k] * b[k,j]
#intervalo = time.time() - inicio
#print('CPU con Python en s = ',intervalo)

# CÁLCULO CON CON CPU Y NUMPY
inicio = time.time()
result = np.dot(a,b)
intervalo = time.time() - inicio
print('CPU con Numpy en s = ',intervalo)


# CÁLCULO CON CON GPU y TENSORFLOW
ta = tf.convert_to_tensor(a)
tb = tf.convert_to_tensor(b)
inicio = time.time()


#result = tf.tensordot(a, b, axes =1, name=None)
result = tf.math.multiply(ta,tb)
intervalo = time.time() - inicio
print('GPU con TensorFlow en s = ',intervalo)