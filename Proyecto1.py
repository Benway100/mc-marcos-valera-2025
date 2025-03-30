import tkinter as tk
import customtkinter as ctk
import struct


ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue")

class CalculadoraBinaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("700x600")
        
     
        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Calculadora de Operaciones Binarias", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=10)
        
    
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill="x", padx=20, pady=10)
 
        self.entrada_label = ctk.CTkLabel(
            self.input_frame, 
            text="Expresión:", 
            font=ctk.CTkFont(size=14)
        )
        self.entrada_label.pack(side="left", padx=10)
        
        self.entrada = ctk.CTkEntry(
            self.input_frame, 
            width=400, 
            height=40, 
            font=ctk.CTkFont(size=16),
            placeholder_text="Ej: 4+5*2 o 4.5+5/2-8"
        )
        self.entrada.pack(side="left", padx=10)
        self.entrada.focus_set()
        
   
        self.calcular_btn = ctk.CTkButton(
            self.input_frame,
            text="Calcular",
            font=ctk.CTkFont(size=14),
            command=self.calcular,
            width=100,
            height=40
        )
        self.calcular_btn.pack(side="left", padx=10)
 
        self.resultado_frame = ctk.CTkFrame(self.main_frame)
        self.resultado_frame.pack(fill="x", padx=20, pady=10)
        
 
        self.resultado_label = ctk.CTkLabel(
            self.resultado_frame,
            text="Resultado:",
            font=ctk.CTkFont(size=14)
        )
        self.resultado_label.pack(side="left", padx=10)
        
        self.resultado = ctk.CTkLabel(
            self.resultado_frame,
            text="",
            font=ctk.CTkFont(size=16, weight="bold"),
            width=200
        )
        self.resultado.pack(side="left", padx=10)
        

        self.binario_frame = ctk.CTkFrame(self.main_frame)
        self.binario_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
     
        self.binario_label = ctk.CTkLabel(
            self.binario_frame,
            text="Representación Binaria:",
            font=ctk.CTkFont(size=14)
        )
        self.binario_label.pack(pady=5)
   
        self.binario_text = ctk.CTkTextbox(
            self.binario_frame,
            font=ctk.CTkFont(family="Courier", size=12),
            wrap="word",
            height=350
        )
        self.binario_text.pack(fill="both", expand=True, padx=10, pady=10)
        

        self.entrada.bind("<Return>", lambda event: self.calcular())
    
    def calcular(self):
        try:
            expresion = self.entrada.get().strip()
            if not expresion:
                self.mostrar_error("Por favor, ingrese una expresión")
                return
                
            resultado, representacion = self.evaluar_expresion(expresion)
            
            # Mostrar resultado
            if isinstance(resultado, float):
                self.resultado.configure(text=str(resultado))
            else:
                self.resultado.configure(text=str(int(resultado)))
            
           
            self.binario_text.delete("0.0", "end")
            self.binario_text.insert("0.0", representacion)
                
        except Exception as e:
            self.mostrar_error(f"Error: {str(e)}")
    
    def mostrar_error(self, mensaje):
        self.resultado.configure(text=mensaje)
        self.binario_text.delete("0.0", "end")
        self.binario_text.insert("0.0", mensaje)
    
    def evaluar_expresion(self, expresion):
       
        tokens = self.tokenizar(expresion)
        
      
        postfijo = self.infix_a_postfijo(tokens)
        
      
        resultado, detalles = self.evaluar_postfijo(postfijo)
        
        return resultado, detalles
    
    def tokenizar(self, expresion):
        #Divide la expresión en tokens (números y operadores)
        tokens = []
        i = 0
        
        while i < len(expresion):
            
            if expresion[i].isdigit() or expresion[i] == '.':
                
                numero = ""
                while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
                    numero += expresion[i]
                    i += 1
                
                # Convertir a entero o flotante según corresponda
                if '.' in numero:
                    tokens.append(float(numero))
                else:
                    tokens.append(int(numero))
            
           
            elif expresion[i] in ['+', '-'] and (i == 0 or expresion[i-1] in ['+', '-', '*', '/']):
                
                numero = expresion[i]
                i += 1
                
             
                while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
                    numero += expresion[i]
                    i += 1
                
               
                if '.' in numero:
                    tokens.append(float(numero))
                else:
                    tokens.append(int(numero))
            
       
            elif expresion[i] in ['+', '-', '*', '/']:
                tokens.append(expresion[i])
                i += 1
            
           
            elif expresion[i].isspace():
                i += 1
            
          
            else:
                raise ValueError(f"Carácter no válido: '{expresion[i]}'")
        
        return tokens
    
    def infix_a_postfijo(self, tokens):
        
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        salida = []
        operadores = []
        
        for token in tokens:
            
            if isinstance(token, (int, float)):
                salida.append(token)
            
       
            elif token in precedencia:
              
                while (operadores and operadores[-1] in precedencia and 
                      precedencia[operadores[-1]] >= precedencia[token]):
                    salida.append(operadores.pop())
                
             
                operadores.append(token)
        
    
        while operadores:
            salida.append(operadores.pop())
        
        return salida
    
    def evaluar_postfijo(self, postfijo):
        #Evalúa una expresión en notación postfija y retorna el resultado y su representación binaria
        pila = []
        hay_float = any(isinstance(token, float) for token in postfijo)
        pasos = []
        
        for token in postfijo:
            if isinstance(token, (int, float)):
              
                if isinstance(token, float) or hay_float:
                   
                    bin_repr = self.numero_a_lista_binaria_float(token)
                    bin_str = self.mostrar_ieee754(bin_repr, token)
                    pila.append((token, True, bin_repr))
                else:
                  
                    bin_repr = self.numero_a_lista_binaria_int(token)
                    bin_str = self.mostrar_complemento2(bin_repr, token)
                    pila.append((token, False, bin_repr))
            else:
            
                b, b_es_float, b_bin = pila.pop()
                a, a_es_float, a_bin = pila.pop()
                
        
                es_float = a_es_float or b_es_float or hay_float
                
     
                if token == '+':
                    resultado = a + b
                elif token == '-':
                    resultado = a - b
                elif token == '*':
                    resultado = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("División por cero")
                    resultado = a / b
            
                    if not es_float and a % b != 0:
                        es_float = True
                
                if es_float:
                 
                    if isinstance(resultado, int):
                        resultado = float(resultado)
                    bin_repr = self.numero_a_lista_binaria_float(resultado)
                    bin_str = self.mostrar_ieee754(bin_repr, resultado)
                else:
                
                    resultado = int(resultado)
                    bin_repr = self.numero_a_lista_binaria_int(resultado)
                    bin_str = self.mostrar_complemento2(bin_repr, resultado)
                
 
                paso = f"Operación: {a} {token} {b} = {resultado}\n"
                if es_float:
                    paso += f"Representación IEEE-754 del resultado:\n{bin_str}\n"
                else:
                    paso += f"Representación Complemento a 2 del resultado:\n{bin_str}\n"
                pasos.append(paso)
                

                pila.append((resultado, es_float, bin_repr))
        
        if len(pila) != 1:
            raise ValueError("Expresión no válida")
        
        resultado, es_float, bin_repr = pila[0]
        

        detalles = "Detalles de la evaluación:\n\n"
        

        for i, paso in enumerate(pasos):
            detalles += f"Paso {i+1}:\n{paso}\n"

        detalles += f"\nResultado final: {resultado}\n"
        if es_float:
            detalles += f"Representación IEEE-754 (32 bits):\n{self.mostrar_ieee754(bin_repr, resultado)}\n"
        else:
            detalles += f"Representación Complemento a 2 (32 bits):\n{self.mostrar_complemento2(bin_repr, resultado)}\n"
        
        return resultado, detalles
    
    def numero_a_lista_binaria_int(self, n):
        #Convierte un entero a una lista binaria de 32 bits en complemento a 2

        bits = [0] * 32
        
        if n < 0:

            valor_positivo = -n
            for i in range(31, -1, -1):
                bits[31-i] = (valor_positivo >> i) & 1
            

            for i in range(32):
                bits[i] = 1 - bits[i]
   
            carry = 1
            for i in range(31, -1, -1):
                sum_bit = bits[i] + carry
                bits[i] = sum_bit % 2
                carry = sum_bit // 2
        else:
    
            for i in range(31, -1, -1):
                bits[31-i] = (n >> i) & 1
        
        return bits
    
    def numero_a_lista_binaria_float(self, n):
 
        
        packed = struct.pack('>f', n)
        
        
        bits = []
        for byte in packed:
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)
        
        return bits
    
    def mostrar_complemento2(self, bits, valor_original=None):
        

      
        if len(bits) != 32:
            raise ValueError("La lista debe tener 32 bits")
        
      
        bit_str = ''.join(str(bit) for bit in bits)
        
   
        resultado = ""
        if valor_original is not None:
            resultado += f"Valor decimal: {valor_original}\n"
        
        resultado += "Representación en complemento a 2 (32 bits):\n"
 
        for i in range(0, 32, 8):
            bloque = bit_str[i:i+8]
            resultado += f"Bits {i}-{i+7}: {bloque}\n"
        
   
        resultado += f"\nBinario completo: {' '.join(bit_str[i:i+8] for i in range(0, len(bit_str), 8))}"
        
        return resultado
    
    def mostrar_ieee754(self, bits, valor_original=None):
      
        if len(bits) != 32:
            raise ValueError("La lista debe tener 32 bits")
        
      
        signo = bits[0]
        exponente = bits[1:9]
        mantisa = bits[9:]
        

        signo_str = str(signo)
        exponente_str = ''.join(str(bit) for bit in exponente)
        mantisa_str = ''.join(str(bit) for bit in mantisa)
        

        resultado = ""
        if valor_original is not None:
            resultado += f"Valor decimal: {valor_original}\n"
        
        resultado += "Representación IEEE-754 (32 bits):\n"
        resultado += f"Signo (1 bit): {signo_str}\n"
        resultado += f"Exponente (8 bits): {exponente_str}\n"
        resultado += f"Mantisa (23 bits): {mantisa_str}\n"
        

        exp_valor = sum(exponente[i] * (2 ** (7-i)) for i in range(8)) - 127
        mantisa_valor = 1.0 + sum(mantisa[i] * (2 ** (-i-1)) for i in range(23))
        
        resultado += f"\nValor exponente: {exp_valor} (sin sesgo: {exp_valor+127})\n"
        resultado += f"Valor mantisa: {mantisa_valor}\n"
        

        valor = (-1)**signo * mantisa_valor * (2**exp_valor)
        resultado += f"Valor calculado desde binario: {valor}"
        
        return resultado


if __name__ == "__main__":
    root = ctk.CTk()
    app = CalculadoraBinaria(root)
    root.mainloop()