i = 0
p = 2
soma = 0
while i < 50:
    if p % 2 == 0:
        soma += p
        i+= 1
    p += 1
print("A soma dos 50 primeiros numeros pares e de", soma)
