import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import copy

x1=np.array([1,1,2,3,-1.5,2,3,3])
x2=np.array([0,0.5,0.5,1,-1.2,1.5,1.50,0.5])
y=np.array([0.2,3,-0.8,-0.4,3.5,3.6,0.5,-1])

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

a = [[len(x1),sum(x1),sum(x2)], [sum(x1),sum(x1**2), sum(x1*x2)], [sum(x2), sum(x1*x2), sum(x2**2)]]
b = [sum(y),sum(x1*y),sum(x2*y)]
x_resut = gaussJordan(a, b)


print("Respuesta:")
for i in range(len(x_resut)):
    print("a" + str(i), "=", x_resut[i])

x_vals1=np.linspace(min(x1),max(x1),200)
x_vals2=np.linspace(min(x2),max(x2),200)
x1_vals,x2_vals=np.meshgrid(x_vals1,x_vals2)

y_pred=x_resut[0]+(x_resut[1]*x1_vals)+(x_resut[2]*(x2_vals))
Sr = np.sum((y - (x_resut[0] + (x_resut[1] * x1) + (x_resut[2] * x2)))**2)
St = np.sum((y - np.mean(y))**2)
r_2 = (St - Sr) / St
r = np.sqrt(r_2) * 100
print(f"Sr = {Sr}")
print(f"St = {St}")
print(f"r^2 = {r_2}")
print(f"r = {r}%")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc=ax.scatter3D(x1,x2,y,c="g",cmap="viridis",label="Datos")
ax.plot_surface(x1_vals,x2_vals,y_pred, color='b', alpha=0.5)

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')


plt.show()
