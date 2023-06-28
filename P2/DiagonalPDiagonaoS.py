def criarMatriz(mat):
    for i in range(0, 3):
        mat.append(0)
        mat[i] = []
        for j in range(0, 3):
            mat[i].append(int(input("n: ")))
    return mat
                                
def diagonalP(mat):
    soma = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                soma += mat[i][j]
    return soma

def diagonalS(mat):
    soma = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if i + j == 3 - 1:
                soma += mat[i][j]
    return soma

mat = []
mat = criarMatriz(mat)
for i in range(0, 3):
    for j in range(0, 3):
        print(mat[i][j], end=" ")
    print()
DP = diagonalP(mat)
print(DP)
ds = diagonalS(mat)
print(ds)
