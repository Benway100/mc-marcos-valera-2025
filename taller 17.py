import matplotlib.pyplot as plt
import numpy as np


x1 = [1, 2, 3, 4, 5, 6, 7, 8]
y = [7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1]


xy=0
x2=0
for i in range(len(x1)):
    xy+=x1[i]*y[i]
    x2+=x1[i]**2

a1=((len(x1)*xy)-sum(x1)*sum(y))/((len(x1)*(x2))-sum(x1)**2)
a0=(sum(y)/len(y))-a1*(sum(x1)/len(x1))
y_pred = [a1 * xi + a0 for xi in x1]

plt.scatter(x1, y, color='b', label=f'Datos originales')
plt.plot(x1, y_pred, color='r', label=f'Linea de regresion')
plt.title('Gráfica de y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
