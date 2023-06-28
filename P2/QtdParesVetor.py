def criarVetor(vet):
    for i in range(0, TAM):
        vet[i] = i
    return vet

def qtdPares(vet):
    contP = 0
    for i in range(0, TAM):
        if vet[i] % 2 == 0:
            contP += 1
    return contP

TAM = 40
vet = [0]*TAM
vet = criarVetor(vet)
qtdp = qtdPares(vet)
print(qtdp)
