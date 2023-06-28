def criarVetor(vet):
    j = 1
    for i in range(0, TAM):
        vet[i] = j
        j += 2
    return vet
        

TAM = 10
vet = [0]*TAM
vet = criarVetor(vet)
print(vet)
