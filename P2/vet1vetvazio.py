def criarVet(vet):
    for i in range(0,6):
        vet[i] = i+1
    return vet

def preencher(vet1, vet2):
    tam = len(vet1)// 2
    m = 0
    j = 0
    n = 0
    for i in range(0,6):
        if i < tam:
            vet2[i] = vet1[len(vet1) - 1 - j]
            j += 1
        else:
            vet2[i] = vet1[n]
            n += 1
    return vet2

vet1 = [0]*6
vet2 = [0]*6
vet1 = criarVet(vet1)
vet2 = preencher(vet1, vet2)
print(vet1)
print(vet2)
