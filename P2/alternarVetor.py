def criarVet(vet):
    for i in range(0, 12):
        vet[i] = i+1
    return vet

def inverter(vet):
    tam = len(vet)
    aux = 0
    j = 0
    for i in range(0, tam//2, 2):
        aux = vet[i + 1]
        vet[i + 1] = vet[i]
        vet[i] = aux
    for i in range(0, tam //4):
        aux = vet[i + (tam//2)]
        vet[i + (tam//2)] = vet[tam - j - 1]
        vet[tam - j - 1] = aux
        j += 1
    return vet

vet = [0]*12
vet = criarVet(vet)
print(vet)
vet = inverter(vet)
print(vet)
