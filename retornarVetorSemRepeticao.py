def semRepeticao(vet):
    vetAux = []
    for i in range(0, len(vet)):
        achou = False
        for j in range(0, len(vetAux)):
            if vet[i] == vetAux[j]:
                achou = True
        if not achou:
            vetAux.append(vet[i])
    return vetAux
                   


vet = [0]*5
vetN = [0]*5
num = 0
for i in range(0, 5):
    num = int(input("Digite um valor para o vetor: "))
    vet[i] = num
print(vet)
vetN = semRepeticao(vet)
print(vetN)
