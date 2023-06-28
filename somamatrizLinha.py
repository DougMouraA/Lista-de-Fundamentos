mat = []
totalL = 0
somaP = 0
for i in range(0,3):
    mat.append(0)
    mat[i] = []
    for j in range(0,3):
        mat[i].append(int(input("Digite um valor: ")))
        totalL += mat[i][j]
        if mat[i][j] % 2 == 0:
            somaP += mat[i][j]
print(mat)
print(totalL)
print(somaP)
