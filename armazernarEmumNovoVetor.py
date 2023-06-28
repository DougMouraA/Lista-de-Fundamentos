vetFinal = [0]*20
vet1 = [0]*10
vet2 = [0]*10
num = 0
for i in range(0, len(vet1)):
    num = int(input("Digite o valor para o primeiro vetor: "))
    vet1[i] = num
num = 0
for j in range(0, len(vet2)):
    num = int(input("Digite o valor para o segundo vetor: "))
    vet2[j] = num
l = 0
m = 0
for k in range(0, len(vetFinal)):
    if k < 10:
        vetFinal[k] = vet1[l]
        l += 1
    else:
        vetFinal[k] = vet2[m]
        m += 1
print(vet1)
print(vet2)
print(vetFinal)
