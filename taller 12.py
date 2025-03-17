import sympy as sp
#Punto 1
x=sp.Symbol('x')
funcion= 1.1*x**4 - 1.9*x**3 + 1.2*x**2 - 2*x + 4
derivada1=sp.diff(funcion,x).subs(x,1.4)

result=abs(derivada1)*0.05
print(f"El error resultande de la funcion {funcion} con x෤ = 1,4 con un error ∆x෤ = 0,05, es de {result}")

#Punto 2
funcion2= sp.cos(x) * sp.ln(2*x)
derivada1_2=sp.diff(funcion2,x).subs(x,60)

result= abs(derivada1_2.evalf())*0.005
print(f"El error resultande de la funcion {funcion2} con x෤ = π/3 con un error ∆x෤ = 0,005, es de {result}")