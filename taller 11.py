import sympy as sp

# Definir la variable y función
x = sp.symbols("x")
f = 0.25*x**4 - 0.75*x**2 + 4.5
h = 0.1

# PRIMERA DERIVADA
print("Primer Punto")
print("Primera diferencia finita dividida hacia adelante")
fxi = f.subs(x, 0.6)
fxi1 = f.subs(x, 0.7)
result_adelante = (fxi1 - fxi) / h
print(result_adelante, "\n")

print("Primera diferencia finita dividida hacia atrás")
funcionxi_atras = f.subs(x, 0.6)
funcionxi1_atras = f.subs(x, 0.5)
result_atras = (funcionxi_atras - funcionxi1_atras) / h
print(result_atras, "\n")

print("Primera diferencia finita dividida centrada")
funcionxi_centrada = f.subs(x, 0.7)
funcionxi1_centrada = f.subs(x, 0.5)
result_centrada = (funcionxi_centrada - funcionxi1_centrada) / (2*h)  
print(result_centrada, "\n")

print("Derivada Real")
deri1 = sp.diff(f, x).subs(x, 0.6)
print(deri1, "\n")

print("--------------------------------------------------------------------------------------------------")

# SEGUNDA DERIVADA
print("Segunda diferencia finita dividida hacia adelante")
funcion_2_hacia_adelantexi2 = f.subs(x, 0.8)
funcion_2_hacia_adelantexi1 = f.subs(x, 0.7)
funcion_2_hacia_adelantexi = f.subs(x, 0.6)
result_adelante2 = (funcion_2_hacia_adelantexi2 - 2*funcion_2_hacia_adelantexi1 + funcion_2_hacia_adelantexi) / h**2
print(result_adelante2, "\n")

print("Segunda diferencia finita dividida hacia atrás")
funcion_2_atras_adelantexi = f.subs(x, 0.6)
funcion_2_atras_adelantexi1 = f.subs(x, 0.5)
funcion_2_atras_adelantexi2 = f.subs(x, 0.4)
result_atras2 = (funcion_2_atras_adelantexi - 2*funcion_2_atras_adelantexi1 + funcion_2_atras_adelantexi2) / h**2
print(result_atras2, "\n")

print("Segunda diferencia finita dividida centrada")
result_centro = (f.subs(x, 0.7) - 2*f.subs(x, 0.6) + f.subs(x, 0.5)) / h**2  
print(result_centro, "\n")

d2 = sp.diff(f, x, 2).subs(x, 0.6)
print(f"Segunda derivada real\n{d2}\n")

print("---------------------------------------------------------------------------------------------------")
print("Segundo Punto")
h = 0.05

print("Primera diferencia finita dividida centrada")
funcion_centro1_x1 = f.subs(x, 0.65)
funcion_centro_x_1 = f.subs(x, 0.55)
result_centro1 = (funcion_centro1_x1 - funcion_centro_x_1) / (2*h)  
print(result_centro1, "\n")

print("Segunda diferencia finita dividida centrada")
funcion2_centro1_x1 = f.subs(x, 0.65)
funcion2_centro_x_1 = f.subs(x, 0.55)
funcion2_centro1_x = f.subs(x, 0.6)
result_centro2 = (funcion2_centro1_x1 - 2*funcion2_centro1_x + funcion2_centro_x_1) / h**2 
print(result_centro2, "\n")

print("Derivada Real")
deri1 = sp.diff(f, x).subs(x, 0.6)
print(deri1, "\n")
