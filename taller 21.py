import numpy as np
import matplotlib.pyplot as plt
import copy

x=np.array([0,2,4,6,8,10,12])
y=np.array([7.5,1.8,-1,-1.8,-1.2,2.2,7.2])

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    for i in range(n):
        pivote = a[i][i]
        
        #Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        #Reducción
        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
    
    return b

a = [[len(x),sum(x),sum(x**2)], [sum(x),sum(x**2), sum(x**3)], [sum(x**2), sum(x**3), sum(x**4)]]
b = [sum(y),sum(x*y),sum((x**2)*y)]
x_resut = gaussJordan(a, b)

x_vals=np.linspace(min(x),max(x),200)
y_pred=x_resut[0]+(x_resut[1]*x_vals)+(x_resut[2]*(x_vals**2))
print("Respuesta:")
for i in range(len(x_resut)):
    print("a" + str(i), "=", x_resut[i])

Sr=0
for i in range(len(x)):
    Sr+=(y[i]-x_resut[0]-(x_resut[1]*x[i])-(x_resut[2])*(x[i]**2))**2
St=0
for i in range(len(x)):
    St=(y[i]-np.mean(y))**2

r_2=(St-Sr)/St
r=np.sqrt(r_2)*100
print(f"Sr = {Sr}")
print(f"St = {St}")
print(f"r^2 = {r_2}")
print(f"r = {r}%")

plt.scatter(x, y, color='b', label=f'Datos originales')
plt.plot(x_vals, y_pred, color='r', label=f'Linea de regresion')
plt.title('Regresion lineal.')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

