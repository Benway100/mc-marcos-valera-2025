import sympy as sp
import math
#Punto 1
x = sp.symbols('x')
f = 0.3*x**3 - 1.8*x**2 + 2.5*x - 1
taylor_series = sp.series(f, x, 0.4, 4).removeO()
numerical_value = taylor_series.evalf(subs={x: 0.5})

print(numerical_value)

#punto 2
f = 1.4*(math.e)**x  - 3.2*x + 2.4
taylor = sp.series(f, x, 0.6, 4).removeO()
numerical = taylor.evalf(subs={x: 0.65})

print(numerical)
