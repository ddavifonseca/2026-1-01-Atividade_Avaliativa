n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))
soma = n1+n2+n3+n4
media = soma/4
if media >= 6:
    situação = "Aprovado(a)!"
else: 
    situação = "Reprovado(a)."
print(f"A média é {media}\nSituação: {situação}")