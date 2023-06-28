def criarVetor(vet):
    n = 0
    for i in range(0, len(vet)):
        n = int(input("Preecha o vetor: "))
        vet[i] = n
    return vet

def preencherVetFinal(vetfinal, vet1, vet2):
    j = 0
    for i in range(0, len(vetfinal)):
        if i < 10:
            vetfinal[i] = vet1[i]
        else:
            vetfinal[i] = vet2[j]
            j += 1          
    return vetfinal

vetfinal = [0]*20
vet1 = [0]*10
vet2 = [0]*10
vet1 = criarVetor(vet1)
vet2 = criarVetor(vet2)
vetfinal = preencherVetFinal(vetfinal, vet1, vet2)
print(vet1)
print(vet2)
print(vetfinal)
