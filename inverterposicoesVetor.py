aux = 0
vet = []
for i in range(0, 16):
    vet.append(i)
print (vet)
for j in range(0, 16 // 2):
    aux = vet[j]
    vet[j] = vet[15 - j]
    vet[15 - j] = aux
print(vet)    
