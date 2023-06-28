vet1 = []
vet2 = []
num = int(input("Digite um valor: "))
while num >= 0:
    vet1.append(num)
    num = int(input("Digite um valor: "))
print(vet1)
num = int(input("Digite um valor: "))
while num >= 0:
    vet2.append(num)
    num = int(input("Digite um valor: "))
print(vet2)
for i in range(0, len(vet1)):
    for j in range (0, len(vet2)):
        if vet1[i] == vet2[j]:
            print(vet1[i])
