def criarVet(vet):
    vet = [0]*TAM
    num = 0
    for i in range(0, TAM):
        num = int(input("Elem: "))
        vet[i] = num
    return vet


def emOrdem(vet):
    for i in range(0, TAM-1):
        if vet[i+1] < vet[i]:
            return False
        return True


TAM = 5
vet = []
vet = criarVet(vet)
if not emOrdem(vet):
    print("Nao esta ordenado")
else:
    print("Esta ordenado")
