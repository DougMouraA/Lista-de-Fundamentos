vet1 = []
nvet = []
num = int(input("Digite um valor: "))
while num >= 0:
    vet1.append(num)
    num = int(input("Digite um valor: "))
print(vet1)
for i in range(0, len(vet1)):
    if i % 2 == 0:
        nvet.append(vet1[i]*2)
    else:
        nvet.append((vet1[i]*3) - 1)
print(nvet)
