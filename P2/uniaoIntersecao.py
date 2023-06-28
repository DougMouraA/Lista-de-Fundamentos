def criarVet(vet):
    n = 0
    for i in range(0, TAM):
        n = int(input("Preencha o vetor: "))
        vet[i] = n
    return vet

def uniaoVetor(vet1, vet2, vetU):
    j = 0
    for i in range(0, 20):
        if i < 10:
            vetU[i] = vet1[i]
        else:
            vetU[i] = vet2[j]
            j += 1
    return vetU

def intersecaoVet(vet1, vet2, vetI):
    for i in range(0, len(vet1)):
        for j in range(0, len(vet2)):
            if vet1[i] == vet2[j]:
                vetI[i] = vet1[i]
    return vetI

TAM = 10
vet1 = [0]*TAM
vet2 = [0]*TAM
vetU = [0]*20
vetI = [0]*TAM
vet1 = criarVet(vet1)
vet2 = criarVet(vet2)
vetU = uniaoVetor(vet1, vet2, vetU)
vetI = intersecaoVet(vet1, vet2, vetI)
print(vetU)
print(vetI)
