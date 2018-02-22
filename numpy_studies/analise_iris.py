import numpy as np
import matplotlib.pyplot as plt


# estrutura dataset
# comprimento sépala | largura sépala | comprimento pétala | largura pétala

#recebendo dados e dividinso por classe de flores
flores = np.genfromtxt("iris.csv",delimiter=',',usecols=(0,1,2,3))
iris_setosa = flores[:50]
iris_versicolours = flores[50:100]
iris_viginica = flores[100:]

col = 2

plt.title('FLORES')
plt.plot(iris_setosa[:,col], Marker='o', Color='Red')
plt.plot(iris_versicolours[:,col], Marker='o', Color='Green')
plt.plot(iris_viginica[:,col], Marker='o', Color='Blue')

plt.show()

print('IRIS SETOSA: ')
print('MÉDIA: ',iris_setosa[:,col].mean())
print('MIN: ',iris_setosa[:,col].min())
print('MAX: ',iris_setosa[:,col].max())

print('IRIS VERSICOLOURS: ')
print('MÉDIA: ',iris_versicolours[:,col].mean())
print('MIN: ',iris_versicolours[:,col].min())
print('MAX: ',iris_versicolours[:,col].max())

print('IRIS VIRGINICA: ')
print('MÉDIA: ',iris_viginica[:,col].mean())
print('MIN: ',iris_viginica[:,col].min())
print('MAX: ',iris_viginica[:,col].max())




