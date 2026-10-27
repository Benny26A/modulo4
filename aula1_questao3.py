n1 = float(input("Introduza a nota n1: "))
n2 = float(input("Introduza a nota n2: "))
n3 = float(input("Introduza a nota n3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")