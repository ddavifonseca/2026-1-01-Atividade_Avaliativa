n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
nall = n1+n2+n3+n4 # soma de todos os valores
media = nall/4 # divisão por 4
menor = min(n1,n2,n3,n4)
maior = max(n1,n2,n3,n4)
diff = maior - menor
print(f"A média aritmética é: {media}")
print(f"A diferença entre o maior e o menor valor é: {diff}")