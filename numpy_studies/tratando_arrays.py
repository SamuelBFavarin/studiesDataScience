import numpy as np


#repartindo arrays
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a = np.array_split(a,2,axis=0)

#for array in a:
#    print(array)

#print('______________')


#criando array de zeros
#print(np.zeros((5,5)))
#print('______________')

#criando matriz identidade

#i = np.eye(10)
#print(i)

#utilizar operações booleanas em matriz
l = np.array([[3,4,5],[10,6,9]])
print(l[l>4])
print(l[l<6])

