def entero_a_binario_complemento_dos(numero):
    if numero < 0:
        numero_binario = bin(abs(numero))[2:].zfill(16)
        numero_binario = ''.join('1' if bit == '0' else '0' for bit in numero_binario)
        numero_binario_complemento_dos = bin(int(numero_binario, 2) + 1)[2:].zfill(16)
        return numero_binario_complemento_dos
    else:
        return bin(numero)[2:].zfill(16)

def suma_binaria_complemento_dos(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    suma = num1 + num2
    suma_binaria = bin(suma)[2:].zfill(16)
    if len(suma_binaria) > 16:
        suma_binaria = suma_binaria[-16:]
    return suma_binaria

print("Por favor, ingrese dos números enteros entre -32.768 y 32.767")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

binario1 = entero_a_binario_complemento_dos(numero1)
binario2 = entero_a_binario_complemento_dos(numero2)

resultado_binario = suma_binaria_complemento_dos(binario1, binario2)
resultado_decimal = int(resultado_binario, 2)

if resultado_binario[0] == '1':
    resultado_complemento_a_uno = ''.join('1' if b == '0' else '0' for b in resultado_binario)
    resultado_complemento_a_dos = int(resultado_complemento_a_uno, 2) + 1
    resultado_decimal = -resultado_complemento_a_dos

print(f"Resultado de la suma en binario: {resultado_binario}")
print(f"Resultado de la suma en decimal: {resultado_decimal}")
