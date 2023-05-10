n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))
n3 = float(input("terceiro numero: "))
menor = 0
meio = 0
maior = 0
if n1 <= n2 and n1 <= n3:
    menor = n1
    if n2 <= n3:
        meio = n2
        maior = n3
    else:
        meio = n3
        maior = n2
elif n2 <= n1 and n2 <= n3:
    menor = n2
    if n1 <= n3:
        meio = n1
        maior = n3
    else:
        meio = n3
        maior = n1
else:
    menor = n3
    if n1 <= n2:
        meio = n1
        maior = n2
    else:
        meio = n2
        maior = n1
print(menor, meio, maior)
