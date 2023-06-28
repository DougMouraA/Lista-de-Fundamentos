def criarVetor(vet):
    num = 0
    for i in range(0, TAM):
        num = int(input("Preecha o vetor: "))
        vet[i] = num
    return vet

def qtdX(vet, x):
    contX = 0
    for i in range(0, TAM):
        if vet[i] == x:
            contX +=1
    return contX
        

TAM = 10
vet = [0]*TAM
vet = criarVetor(vet)
x = int(input("Digite um valor para x: "))
qtd = qtdX(vet, x)
print(qtd)
