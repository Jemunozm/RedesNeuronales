#app_1.6
import numpy as np
#arreglo de tres dimensiiones
m = np.arange(36).reshape(3,4,3)
print("Tipo de dato de m:", m.dtype)
print("Shape (forma) del arreglo de m:",m.shape)
print("Tamaño del arreglo arreglo de m:",m.size)
print("Dimensión del arreglo de m:", m.ndim)
print("m es un arreglo de tres dimensiones:\n",m)
print("\n")
#print("Primera fila (capa fila 0:\n",np.array(m[:,0,0]))
print("Primera fila (capa fila 0):\n",np.array(m[0,:,:]))
print("Segunda fila (capa fila 1):\n",np.array(m[1,:,:]))
print("Tercera fila (capa fila 2):\n",np.array(m[2,:,:]))
print("\n")
print("Primera columna (capa coumna 0):\n",np.array(m[:,0,:]))
print("Segunda columna (capa columna 1):\n",np.array(m[:,1,:]))
print("Tercera columna (capa columna 2):\n",np.array(m[:,2,:]))
print("Cuarta columna (capa columna 3):\n",np.array(m[:,3,:]))
print("\n")
print("Profundidad nivel 0 (capa coumna 0):\n",np.array(m[:,:,0]))
print("Profundidad nivel 1 (capa columna 1):\n",np.array(m[:,:,1]))
print("Produndidad nivel 2 (capa columna 2):\n",np.array(m[:,:,2]))


