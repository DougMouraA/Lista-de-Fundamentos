def criarVet(vet):
    n = 0
    for i in range(0, TAM):
        n = int(input("Vetor: "))
        vet[i] = n
    return vet

def ordenarVet(vet):
    aux = [0]*9
    for i in range(0, TAM):
        if i == 1:
            aux[i] = vet[i]
        else:
            aux[i] = vet[vet[i]]
    return aux

TAM = 9
vet = []
vet = criarVet(vet)
vet = ordenarVet(vet)
print(vet)
