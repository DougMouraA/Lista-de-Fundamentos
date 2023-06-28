def criarMatriz(mat):
    for i in range(0, 5):
        mat.append(0)
        mat[i] = []
        for j in range(0, 5):
            mat[i].append(j)
    return mat       


def maiorElemento(mat):
    maior = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if maior < mat[i][j]:
                maior = mat[i][j]
    return maior

mat = []
mat = criarMatriz(mat)
maior = maiorElemento(mat)
print(mat)
print(maior)
