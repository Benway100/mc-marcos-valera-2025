import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x=sp.symbols("x")
x_n=[1,2,3,4,5]
y=[2,0.5,-2,-3.5,0.5]

def Interpolacion_lagrange(poli):
    fn=0
    for i in range(poli+1):
        l_i=1
        for j in range(poli+1):
            if i!=j:
               l_i*=(x-x_n[j]) / (x_n[i]-x_n[j])
        fn+=l_i*y[i]
    return fn

y_pred3=Interpolacion_lagrange(len(x_n)-1)

print(f"Polinomio:{y_pred3}")
f = sp.lambdify(x, y_pred3, modules=["numpy"])  
x_vals = np.linspace(min(x_n), max(x_n), 200)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=f'Polinomio grado {len(x_n)-1}', color='red')
plt.scatter(x_n, y, color='blue', label='Datos originales')
plt.title('Interpolación de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

