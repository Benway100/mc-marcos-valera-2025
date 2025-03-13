import math
#Punto 1
#A)
datos=[3,5,3,2]
result= 1
for i in datos:
    result*=i
print((result))

#B)
datos=[10,5,3,2]
result= 1
for i in datos:
    result*=i
print((result))

#Punto 2
#A)
letras=26
numeros=10
result=(letras**3)*(numeros**3)
print(result)

#B)
num=26*25*24
letras=10*9*8
print(letras*num)

#punto 3
personas=10
puestos=4
n=math.factorial(personas)

result=n/math.factorial(personas-puestos)
print(result)

#Punto 4
print(2**12)

#Punto 5
#A)
print(math.factorial(9))
#B)
print((math.factorial(5))*(math.factorial(5)))
#C)
print((math.factorial(5))*(math.factorial(4)))