def criarMatriz(mat):
    for i in range(0, 10):
        mat.append(0)
        mat[i] = []
        for j in range(0, 10):
            mat[i].append(j)
    return mat

def somaDif(mat):
    somaP = 0
    somaI = 0
    for i in range(0, 10):
        if mat[3][i] % 2 == 0:
            somaP += mat[3][i]
        if mat[i][7] % 2 != 0:
            somaI += mat[i][7]
    dif = somaP - somaI
    return dif

def diagonalPI(mat):
    for i in range(0, 10):
        print(mat[10 - i - 1][10 - i - 1])

def imprimir(mat):
    for i in range(0, 10):
        for j in range(0, 10):
            print(mat[i][j], end=" ")
        print()

mat = []
mat = criarMatriz(mat)
imprimir(mat)
print("soma dos elementos pares lin3 menos col7", somaDif(mat))
diagonalPI(mat)
