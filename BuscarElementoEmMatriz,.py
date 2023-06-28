soma = 0
vet = []
contX = 0
contY= 0
x = int(input("Digite um valor para X: "))
y = int(input("Digite um valor para Y: "))
for i in range(0, 12):
    vet.append(int(input("Digite um valor para preencher o vetor: ")))
    if vet[i] == x and contX == 0:
        soma += i
        contX += 1
        print(i)
    elif vet[i] == y and contY == 0:
        soma += i
        contY += 1
        print(i)
print(vet)
print(soma)
