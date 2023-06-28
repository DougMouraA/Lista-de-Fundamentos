def criarMatriz(mat):
    for i in range(0, 7):
        mat.append(0)
        mat[i] = []
        for j in range(0, 7):
            mat[i].append(j)
    return mat

def somaLinhaSeis(mat):
    soma = 0
    for j in range(0, 7):
        soma += mat[6][j]
    return soma

def somaColDois(mat):
    soma = 0
    for i in range(0, 7):
        soma += mat[i][2]
    return soma

def somaDiagonalP(mat):
    soma = 0
    for i in range(0, 7):
        for j in range(0, 7):
            if i == j:
                soma += mat[i][j]
    return soma

def linhaCol(mat):
    return mat[3][4]

def somaElemPares(mat):
    soma = 0
    for i in range(0, 7):
        for j in range(0, 7):
            if mat[i][j] %2 ==0:
                soma += mat[i][j]
    return soma
    

mat = []
mat = criarMatriz(mat)
somaLSeis = somaLinhaSeis(mat)
somaColDois = somaColDois(mat)
somaDP = somaDiagonalP(mat)
linhaCol = linhaCol(mat)
somapar = somaElemPares(mat)
for i in range(0,7):
    for j in range(0,7):
        print(mat[i][j],end=" ")
    print()

print(somaLSeis)
print(somaColDois)
print(somaDP)
print(linhaCol)
print(somapar)



