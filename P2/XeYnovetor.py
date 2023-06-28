def criarVetor(vet):
    n = 0
    for i in range(0, TAM):
      n = int(input("valor: "))
      vet[i] = n
    return vet

def somaXY(vet, x, y):
    soma = 0
    for i in range(0, TAM):
        if vet[i] == x:
            soma += i
        elif vet[i] == y:
            soma +=i
    return soma

TAM = 12
vet = [0]*TAM
vet = criarVetor(vet)
x = int(input("Digite o valor de X de 1 a 12: "))
y = int(input("Digite o valor de y de 1 a 12: "))
soma = somaXY(vet, x, y)
print (soma)
