def criarMatriz(mat):
    n = 0
    for i in range(0, 4):
        mat.append(0)
        mat[i] = []
        for j in range(0, 4):
            mat[i].append(int(input("n: ")))
    return mat


def procurarSomar(mat):
    somaT = 0
    for i in range(1, 3):
        for j in range(1, 3):
            soma = 0
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    if p != i or q != j:
                        soma += mat[p][q]
            if soma == 0:
                print(mat[i][j])
                print("i", i, "j", j)
                somaT += mat[i][j]
    return (somaT)

mat = []
mat = criarMatriz(mat)
soma = procurarSomar(mat)
for i in range(0, 4):
    for j in range(0, 4):
        print(mat[i][j], end=" ")
    print()
print("essa e a soma", soma)
