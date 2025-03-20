import sympy as sp
import math
x=sp.symbols('x')
funcion=sp.exp(-x)
a=0

real=math.e**-0.805
print(f"Valor real de la funcion e^-x es {real}")

for i in range(0,16):
    result=(sp.diff(funcion,x,i).subs(x,0.8)/sp.factorial(i))*((0.805-0.8)**i)
    a+=result
    error=(abs(real-a)/real)*100
    print(f"La aproximacion da {a} y el porcentaje de error con respecto al real es {error} %")