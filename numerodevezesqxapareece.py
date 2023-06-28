x = int(input("Digite um valor para X: "))
cont = 0
vet = []
for i in range(0, 10):
    vet.append(int(input("Valor para o vetor: ")))
    if vet[i] == x:
        cont += 1
print(cont)
