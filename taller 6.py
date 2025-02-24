import math

def calcular_coseno_taylor(x):
    epsilon_s= .5e-8*100
   
    termino = 1  
    suma = termino
    n = 1  
    error_relativo = 100  
    
    while error_relativo > epsilon_s:
        
        termino *= -x**2 / ((2*n-1) * (2*n))
        suma += termino
        n += 1
        
        error_relativo = abs(termino / suma) * 100
        
    
    return suma, error_relativo, n

x = float(input("Introduce el valor en radianes: "))


valor_estimado, error, iteraciones = calcular_coseno_taylor(x)

print(f"\nResultado estimado para cos({x}): {valor_estimado}")
print(f"Error aproximado relativo porcentual: {error:.16f}%")
print(f"Número de iteraciones realizadas: {iteraciones}")
