def criarMatriz(mat):
    for i in range(0, 5):
        mat.append(0)
        mat[i] = []
        for j in range(0, 5):
            mat[i].append(j)
    return mat

def mediaCol(mat, vet):
    soma = 0
    for j in range(0, 5):
        soma = 0
        for i in range(0, 5):
            soma += mat[i][j]
        media = soma / 5
        vet[j] = media
    return vet
mat = []
mat = criarMatriz(mat)
vet = [0]*5
vet = mediaCol(mat, vet)
for i in range(0, 5):
    for j in range(0, 5):
        print(mat[i][j], end=" ")
    print()
print(vet)
    
