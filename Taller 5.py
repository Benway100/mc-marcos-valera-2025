import math
#Punto 1
#A)
print("Punto 1")
a=math.comb(20,8)
print(f"A) La seleccion se puede tomar de {a} maneras distintas")
#B)
b=math.comb(6,3)
c=math.comb(14,5)
print(f"B) Las formas en la que puedo seleccionar las aplicaciones que quiero mantener instaladas es de {b*c} formas")

#Punto 2
#A)
print("Punto 1")
d=math.comb(52,5)
print(f"A) La manera en que se pueden ordenar las 5 cartas de póquer de 52 es de {d} maneras distintas")
#C)

e=math.comb(13,5)
print(f"B) {e} contienen la mano de poquer del mismo palo")

f=math.comb(4,2)
g=math.comb(4,3)
h=math.comb(13,1)
i=math.comb(12,1)
print(f"C) las manos de poquer que contienen tres cartas de una denominacion y dos de otra son {f*g*h*i}")