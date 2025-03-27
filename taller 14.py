import random
import numpy
#PUNTO 1
v1=[]
v2=[]
c=0
n=int(input("Ingrese el tamaño de los vectores: "))
for i in range(n):
    a=random.randint(0,9)
    b=random.randint(0,9)
    v1.append(a)
    v2.append(b)
print(v1,v2)
for i in range (len(v1)):
    c+=v1[i]*v2[i]
print(c)
#PUNTO 2
m1=[]
m2=[]
suma=[]
multi=[]
opeacion=input("1.Suma\n2.Multiplicacion\n3.Salir")


for i in range(4):
    filam1=[]
    filam2=[]
    fimasuma=[]
    for j in range(4):
        f=random.randint(0,9)
        e=random.randint(0,9)
        filam1.append(e)
        filam2.append(f)
        fimasuma.append(e+f)
    m1.append(filam1)
    m2.append(filam2)
    suma.append(fimasuma)
print("Matriz 1")
for i in range(4):
    print(*m1[i],end="\n")
print("Matriz 2")
for i in range(4):
    print(*m2[i],end="\n")
if opeacion=="1":
    print("Suma de matrices")
    for i in range(4):
        print(*suma[i],end="\n")
elif opeacion=="2":
    print("Multiplicacion de matrices")
    multi=numpy.dot(m1,m2)
    print(*multi)
