import random
numa=int(input("Tamaño conjunto A: "))
numb=int(input("Tamaño conjunto B: "))
a={}
while len(a) <numa:
    a[random.randint(0,30)]=None
b={}
while len(b) <numb:
    b[random.randint(0,30)]=None


print(f"Conjunto: {a.keys()}")
print(f"Conjunto: {b.keys()}")
print(f"A U B: {a.keys()|b.keys()}")

if type(a.keys()&b.keys()) is not set:
    print("A ∩ B: {∅}")
    
else:
    print(f"A ∩ B: {a.keys()&b.keys()}")

if type(a.keys()-b.keys()) is not set: 
    print("A - B: {∅}")
else:
    print(f"A - B: {a.keys()-b.keys()}") 


if type(b.keys()-a.keys()) is not set: 
    print("B - A: {∅}")
else:
    print(f"B - A: {b.keys()-a.keys()}") 



if type(a.keys()^b.keys()) is not set: 
    print("A Δ B: {∅}")
else:
    print(f"A Δ B: {a.keys()^b.keys()}") 

