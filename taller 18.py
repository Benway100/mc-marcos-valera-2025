import matplotlib.pyplot as plt
import numpy as np


x = [0,1, 2, 3, 4, 5, 6]
y = [0, 0.5, 2,3.5,4.5,9,13.5]
y_prom=sum(y)/len(y)

xy=0
x2=0
for i in range(len(x)):
    xy+=x[i]*y[i]
    x2+=x[i]**2

a1=((len(x)*xy)-sum(x)*sum(y))/((len(x)*(x2))-sum(x)**2)
a0=(sum(y)/len(y))-a1*(sum(x)/len(x))
y_pred = [a1 * xi + a0 for xi in x]

St=0
for i in y:
    St+=(i-y_prom)**2
Sy=(St/(len(y)-1))**(1/2)

Sr=0
for i in range(len(x)):
    Sr+=(y[i]-a0-a1*x[i])**2
Sy_x=(Sr/(len(y)-2))**(1/2)

r2=(St-Sr)/St
r=((r2)**(1/2))*100

print(f"Desviacion estandar(Sy): {Sy}")
print(f"Error estandar de la estimacion(Sy/x): {Sy_x}")
print(f"Coeficiente de determinacion(r^2): {r2}")
print(f"Coeficiente de correlacion(r %): {r}")
plt.scatter(x, y, color='b', label=f'Datos originales')
plt.plot(x, y_pred, color='r', label=f'Linea de regresion')
plt.title('Gráfica de y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
