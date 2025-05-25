import matplotlib.pyplot as plt
import numpy as np
import copy

def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = b.copy()
    n = len(bAux)

    for i in range(n):
        if aAux[i][i] == 0:
            for k in range(i + 1, n):
                if aAux[k][i] != 0:
                    aAux[i], aAux[k] = aAux[k], aAux[i]
                    bAux[i], bAux[k] = bAux[k], bAux[i]
                    break

        divisor = aAux[i][i]
        for j in range(i, n):
            aAux[i][j] /= divisor
        bAux[i] /= divisor

        for j in range(n):
            if j != i:
                factor = aAux[j][i]
                for k in range(n):
                    aAux[j][k] -= aAux[i][k] * factor
                bAux[j] -= bAux[i] * factor

    return bAux

def trazadoresCubicos(x, y):
    n = len(x)
    a = []
    b = [0] * (n - 2)

    for i in range(n - 2):
        a.append(b.copy())

    for i in range(1, n - 1):
        if i > 1:
            a[i - 1][i - 2] = x[i] - x[i - 1]
        a[i - 1][i - 1] = 2 * (x[i + 1] - x[i - 1])
        if i < n - 2:
            a[i - 1][i] = x[i + 1] - x[i]
        b[i - 1] = (6 / (x[i + 1] - x[i])) * (y[i + 1] - y[i]) + \
                   (6 / (x[i] - x[i - 1])) * (y[i - 1] - y[i])

    rtaAux = gaussJordan(a, b)
    f2 = [0] + rtaAux + [0]

    coeficientes = []

    for i in range(1, n):
        t1 = f2[i - 1] / (6 * (x[i] - x[i - 1]))
        t2 = f2[i] / (6 * (x[i] - x[i - 1]))
        t3 = y[i - 1] / (x[i] - x[i - 1]) - f2[i - 1] * (x[i] - x[i - 1]) / 6
        t4 = y[i] / (x[i] - x[i - 1]) - f2[i] * (x[i] - x[i - 1]) / 6

        arrCoef = [0] * 4
        arrCoef[0] = t1 * x[i]**3 - t2 * x[i - 1]**3 + t3 * x[i] - t4 * x[i - 1]
        arrCoef[1] = -t1 * 3 * x[i]**2 + t2 * 3 * x[i - 1]**2 - t3 + t4
        arrCoef[2] = t1 * 3 * x[i] - t2 * 3 * x[i - 1]
        arrCoef[3] = -t1 + t2

        coeficientes.append(arrCoef)

    return coeficientes

def main():
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 5, 2.5, 4, -1.6, 2]

    coeficientes = trazadoresCubicos(x, y)

    # Graficar los trazadores cúbicos por tramos
    for i, arrCoef in enumerate(coeficientes):
        print('f(x) = ', end='')
        for j in range(4):
            if arrCoef[j] != 0:
                if j > 0 and arrCoef[j] > 0:
                    print('+ ', end='')
                print(arrCoef[j], end='')
                if j == 1:
                    print('x ', end='')
                elif j > 1:
                    print(f'x^{j} ', end='')
                else:
                    print(' ', end='')
        print(f'{{{x[i]} <= x < {x[i+1]}}}')
        if x[i] == 3 and x[i+1] == 4:
            print(arrCoef[0] + arrCoef[1]*3.55 + arrCoef[2]*3.55**2 + arrCoef[3]*3.55**3)

        x_vals = np.linspace(x[i], x[i+1], 100)
        y_vals = arrCoef[0] + arrCoef[1]*x_vals + arrCoef[2]*x_vals**2 + arrCoef[3]*x_vals**3
        plt.plot(x_vals, y_vals, label=f'Tramo {i+1}')

    # Agregar puntos originales en rojo
    plt.scatter(x, y, color='red', label='Puntos', zorder=5)

    # Configuración general del gráfico
    plt.title("Interpolación con Trazadores Cúbicos")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
