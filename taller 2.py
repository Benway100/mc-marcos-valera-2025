u=set()
a=set()
while True:
    c=input("Ingrese el conjunto universal (ingrese la  letra n para terminar): ")
    if c == "n":
        break
    else:
        u.add(int(c))
while True:   
    d=input("Ingrese el conjunto A (ingrese la  letra n para terminar): ")
    if d == "n":
        break
    else:
        a.add(int(d))
if u.issuperset(a):
    print("A es subconjunto de U")
    print(f"(U  ∩ A)U A: {(u.intersection(a)).union(a)}")
    print(f"(U - A) ∩ A: {(u.difference(a)).intersection(a)}")
    print(f"(U Δ A) - A: {(u.symmetric_difference(a)).difference(a)}")
else:
    print("A no es subconjunto de U")
    

