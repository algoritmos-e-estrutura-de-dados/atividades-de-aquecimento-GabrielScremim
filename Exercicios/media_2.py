a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
c = float(input("Nota 3: "))

notaA = (a * 2)
notaB = (b * 3)
notaC = (c * 5)
nota = ( notaA + notaB + notaC)
notaFinal = (nota / 10)

print(f"MEDIA = {notaFinal:,.1f}")
