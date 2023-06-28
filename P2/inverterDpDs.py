def criarMatriz(mat):
    for i in range(0, 4):
        mat.append(0)
        mat[i] = []
        for j in range(0, 4):
            mat[i].append(j)
    return mat

def inverter(mat):
    for i in range(0, 4):
        mat[i][i] = mat[i][3-i]
        mat[i][3-i] = mat[i][i]
    return mat
mat = []
mat = criarMatriz(mat)
for i in range(0, 4):
    for j in range(0, 4):
        print(mat[i][j], end=" ")
    print()
print("\n")
mat = inverter(mat)
for i in range(0, 4):
    for j in range(0, 4):
        print(mat[i][j], end=" ")
    print()
