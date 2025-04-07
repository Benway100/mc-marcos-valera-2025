import copy
import numpy as np

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print("|", b[i])
    print()

def gaussJordan(ao):
    a = copy.deepcopy(ao)
    n = len(a)
    b = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    imprimirSistema(a, b, "Matriz aumentada inicial [A | I]")

    for i in range(n):
        pivote = a[i][i]
        if pivote == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    pivote = a[i][i]
                    break
            else:
                raise ValueError(f"No se puede resolver el sistema, pivote en la posición ({i},{i}) es cero y no hay fila válida para intercambiar.")
        
        for j in range(n):
            a[i][j] /= pivote
        b[i] = [val / pivote for val in b[i]]
        imprimirSistema(a, b, "División")

        for k in range(n):
            if i != k:
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] = [b[k][j] + b[i][j] * valorAux for j in range(n)]
        imprimirSistema(a, b, "Reducción")

    return b

def multiplicarMatrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
    return result

def verificarIdentidad(a, inversa):
    identidad = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    resultado = multiplicarMatrices(a, inversa)
    
    print("\nResultado de multiplicar A por su inversa:")
    for row in resultado:
        print(row)
    
    for i in range(len(identidad)):
        for j in range(len(identidad)):
            if abs(resultado[i][j] - identidad[i][j]) > 1e-6:
                return False
    return True

a = [[2, 2, 0], [4, -1, 0], [3, 2, -2]]
inversa = gaussJordan(a)

print("\nInversa de la matriz A usando Gauss-Jordan:")
for row in inversa:
    print(row)

if verificarIdentidad(a, inversa):
    print("\nLa multiplicación de A por su inversa es la matriz identidad.")
else:
    print("\nLa multiplicación de A por su inversa NO es la matriz identidad.")
