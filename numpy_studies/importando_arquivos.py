import numpy as np

#importando arquivos txt sem dados faltantes
array = np.loadtxt('dados.txt', skiprows=1, unpack=True)
print(array)


#importando arquivos txt com dados faltantes
arr = np.genfromtxt('dados2.txt', skip_header=1, filling_values=0)
print(arr)


