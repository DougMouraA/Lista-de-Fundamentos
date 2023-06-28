vet1 = [0]*15
vet2 = [0]*15
num = 0
soma1 = 0
soma2 = 0
menos1 = 0
menos2 = 0
for i in range(0, len(vet1)):
    num = int(input("Valores para o primeiro Vetor: "))
    vet1[i] = num
    soma1 += vet1[i]
    menos1 -= vet1[i]
for j in range(0, len(vet2)):
    num = int(input("Valores para o segundo Vetor: "))
    vet2[j] = num
    soma2 += vet2[j]
    menos2 -= vet2[j]
print("A soma dos elementos do vetor 1,",soma1,"e a diferenca,",menos1)
print("A soma dos elementos do vetor 2,",soma2,"e a diferenca,",menos2)
