A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
C = float(input("Digite o terceiro valor: "))
pi = 3.14159

print(f"TRIÂNGULO = {(A * C) / 2:,.3}")
print(f"CIRCULO = {pi * (C ** 2):,.3f}")
print(f"TRAPÉZIO = {((A + B) * C / 2):,.3f}")
print(f"QUADRADO = { B ** 2:,.3f}")
print(f"RETÂNGULO = {A * B:,.3f}")