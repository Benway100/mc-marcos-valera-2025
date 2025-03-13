a=int(input("Ingrese el numero en base 10 a convertir: "))
f=a
c=[]
while True:
    if a>0:
        b=a%16
        c.append(b)
        a//=16
    else:
        break
c.reverse()

d=str(c).replace("10","A").replace("11","B").replace("12","C").replace("13","D").replace("14","E").replace("15","F")
print((d[1:-1]).replace(", "," "))
print((hex(f)[2:]).upper())


num = input("Ingrese el número en base 8 a convertir: ")

for digit in num:
    if digit not in "01234567":
        print("El número no es válido para base 8, contiene dígitos inválidos.")
        break
else:
    num_base_10 = 0
    longitud = len(num)
    
    for i in range(longitud):
        num_base_10 += int(num[i]) * (8 ** (longitud - 1 - i))
    
    print(f"El número en base 10 es: {num_base_10}")
