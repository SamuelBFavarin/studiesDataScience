import numpy as np
import matplotlib.pyplot as plt

#define arrays com numpy
a = np.array([10,20,70,45,3,9])
b = np.array([78,79,50,10,2,60])
c = np.array([170,70,70,80,20,50,1])

#insere no final do array
a = np.append(a,180)

#insere na posição do array
b = np.insert(b,0,250)

#printa no gráfico
plt.plot(a, ls='--', marker='s', ms='7', c='blue',label='a')
plt.plot(b, ls='--', marker='^', ms='7', c='red',label='b')
plt.plot(c, ls='--', marker='o', ms='7', c='green',label='c')
plt.legend()
plt.show()


