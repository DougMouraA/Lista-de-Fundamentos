soma = 0
vet = []
cont = 0
contA = 0
contR = 0
for i in range(0, 10):
    vet.append(float(input("Digite a nota: ")))
    soma += vet[i]
    cont += 1
media = soma / cont
print(media)
for j in range(0, 10):
    if vet[j] >= media:
        contA += 1
    else:
        contR += 1

print("Numero de alunos acima da media,", contA)
print("Numero de alunos abaixo da media,", contR)
