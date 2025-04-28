import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5, 6,7,8]
y = [4.5,6.5,7.5,8,8.4,8.8,9,9.3]

x=np.array(x)
y=np.array(y)

y_log=np.log(y)
x_log=np.log(x)
xy=np.sum(x_log*y_log)
x2=np.sum(x_log**2)


a1=((len(x)*xy)-sum(x_log)*sum(y_log))/((len(x)*(x2))-sum(x_log)**2)
a0=(sum(y_log)/len(y))-a1*(sum(x_log)/len(x))

alpha=np.exp(a0)
beta=a1

y_pred = alpha*x**beta


y_prom = np.mean(y)
Sr = np.sum((y - y_pred)**2)
St = np.sum((y - y_prom)**2)
Sy = np.sqrt(St / (len(y) - 1))
Sy_x = np.sqrt(Sr / (len(y) - 2))

r2 = (St - Sr) / St
r = np.sqrt(r2) * 100

print(f"Desviacion estandar(Sy): {Sy}")
print(f"Error estandar de la estimacion(Sy/x): {Sy_x}")
print(f"Coeficiente de determinacion(r^2): {r2}")
print(f"Coeficiente de correlacion(r): {r}%")
plt.scatter(x, y, color='b', label=f'Datos originales')
plt.plot(x, y_pred, color='r', label=f'Linea de regresion')
plt.title('Modelo exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
