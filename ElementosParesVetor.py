contP = 0
vet = []
for i in range(1, 41):
    vet.append(i)
    if vet[i- 1] % 2 == 0:
        contP += 1
print(vet)
print("Quantidade de elementos pares sao:", contP)
