def criarVet(vet):
    n = 0
    for i in range(0, len(vet)):
        n = int(input("Preecha o vetor: "))
        vet[i] = n
    return vet

def somaVetores(vet1, vet2):
    soma = 0
    for i in range(0, len(vet1)):
        soma += vet1[i] + vet2[i]
    return soma

def diferencaVetores(vet1, vet2):
    diferenca = 0
    for i in range(0, len(vet1)):
        diferenca += vet1[i] - vet2[i]
    return diferenca

vet1 = [0]*15
vet2 = [0]*15
vet1 = criarVet(vet1)
vet2 = criarVet(vet2)
soma = somaVetores(vet1, vet2)
diferenca = diferencaVetores(vet1, vet2)
print("A soma entre os elementos dos vetores e de", soma,"e a diferenca e de", diferenca)

