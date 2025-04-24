import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5, 6]
y = [1.5, 2.5, 3.5,4.5,6.5,9]
x=np.array(x)
y=np.array(y)

y_log=np.log(y)
xy=np.sum(x*y_log)
x2=np.sum(x**2)


a1=((len(x)*xy)-sum(x)*sum(y_log))/((len(x)*(x2))-sum(x)**2)
a0=(sum(y_log)/len(y_log))-a1*(sum(x)/len(x))

alpha=np.exp(a0)
beta=a1

y_pred = alpha*(np.exp(beta*x))

Sr = np.sum((y - y_pred) ** 2)  
St = np.sum((y - np.mean(y)) ** 2)  
Sy = np.sqrt(St / (len(x) - 1))         
Sy_x = np.sqrt(Sr / (len(x) - 2))       
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
