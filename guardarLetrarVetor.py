def buscaLetras(frase):
    vetL = []
    for i in range(0, len(frase)):
        if frase[i] != " ":
            vetL.append(frase[i])
    return vetL

def qtdLetras(vet):
    vetNL = []
    for i in range(0, len(vet)):
        cont = 0
        for j in range(0, len(vet)):
            if vet[i] == vet[j]:
                cont += 1
        vetNL.append(cont)
    return vetNL

frase = input("Digite uma Frase: ")
vetL = []
vetNL = []
vetL = buscaLetras(frase)
vetNL = qtdLetras(vetL)
print(vetL)
print(vetNL)
