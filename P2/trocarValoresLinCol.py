def criarMatriz(mat):
    for i in range(0, 4):
        mat.append(0)
        mat[i] = []
        for j in range(0, 4):
            mat[i].append(int(input("n: ")))
    return mat
            
def inverter(mat):
    for i in range(0, 4):
        mat[1][i] = mat[i][3]
        mat[i][3] = mat[1][i]
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
