def criarMatriz(mat):
    for i in range(0, 5):
        mat.append(0)
        mat[i] = []
        for j in range(0, 5):
            mat[i].append(j)
    return mat

def diferencaLinCol(mat1, mat2):
    vet = [0]*5
    for i in range(0, len(mat1)):
        somaL = 0
        for j in range(0, len(mat1)):
            somaL += mat1[i][j]
        vet[i] += somaL
    for m in range (0, len(mat2)):
        somaC = 0
        for n in range(0, len(mat2)):
            somaC += mat2[n][m]
        vet[m] -= somaC
    return vet
mat1 = []
mat2 = []
vet = [0]*5
mat1 = criarMatriz(mat1)
mat2 = criarMatriz(mat2)
print(mat1, mat2)
vet = diferencaLinCol(mat1, mat2)
print(vet)
