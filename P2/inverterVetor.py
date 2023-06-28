def criarVetor(vet):
    for i in range(0, TAM):
        vet[i] = i
    return vet

def inverter(vet):
    aux = 0
    for i in range(0, TAM // 2):
        aux = vet[i]
        vet[i] = vet[TAM - 1]
        vet[TAM - 1] = aux
    return vet

TAM = 16
vet = [0]*TAM
vet = criarVetor(vet)
print(vet)
vet = inverter(vet)
print(vet)
